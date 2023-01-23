from datetime import datetime
import base64
import os
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from PIL import Image
from app import db
from models import SurveyResult
import calculator.constants as const

# Config
calculator_blueprint = Blueprint('calculator', __name__, template_folder='templates')


@calculator_blueprint.route('/calculator')
def calculator():
    """Render calculator page when routed. """
    return render_template('calculator.html', hasNav=True)


@calculator_blueprint.route('/submit', methods=['GET', 'POST'])
def submit():
    """ Calculate a users carbon footprint and return the results page. """
    # Calculate emissions of each section
    # Some sections include emissions from the UK's government
    food = carbonEmissionFood()
    transport = carbonEmissionTransport() + (const.UK_EMISSIONS/3)
    purchasing = carbonEmissionPurchasing() + (const.UK_EMISSIONS/3)
    energy = carbonEmissionEnergy() + (const.UK_EMISSIONS/3)
    # Find total emissions
    totalEmission = food + transport + purchasing + energy

    # Calculate percentage of each section as well as the date and number of trees
    # required to match your emissions
    foodPercent = int(round(calcPercentage(totalEmission, food), 0))
    transportPercent = int(round(calcPercentage(totalEmission, transport), 0))
    purchasingPercent = int(round(calcPercentage(totalEmission, purchasing), 0))
    energyPercent = int(round(calcPercentage(totalEmission, energy), 0))
    date = datetime.today()
    totalEmissionTonne = round(totalEmission * const.KG_TO_TON, 2)
    trees = int(round(totalEmissionTonne / const.TREES, 0))

    return results(totalEmissionTonne, foodPercent, transportPercent
                   , purchasingPercent, energyPercent, trees, date, True)


def carbonEmissionFood():
    """ Calculates the emissions from the food section. """
    # Get the values from the form
    diet = float(request.form.get("food_1"))
    eatingOut = float(request.form.get("food_2"))
    waste = float(request.form.get("food_3"))
    fish = float(request.form.get("food_4_fish")) * const.FISH_EF
    cat = float(request.form.get("food_4_cat")) * const.CAT_EF
    smallDog = float(request.form.get("food_4_small_dog")) * const.SMALL_DOG_EF
    largeDog = float(request.form.get("food_4_large_dog")) * const.LARGE_DOG_EF
    otherSmall = float(request.form.get("food_4_other_small")) * const.OTHER_SMALL
    otherLarge = float(request.form.get("food_4_other_large")) * const.OTHER_LARGE

    # Calculate different emissions for the questions
    dietEmissions = diet * const.YEAR_IN_DAYS
    eatingOutEmissions = const.EATING_OUT_EF * const.YEAR_IN_WEEKS * eatingOut
    wasteEmissions = (waste * const.FOOD_A_YEAR) * const.WASTE_EF
    petEmissions = fish + cat + smallDog + largeDog + otherSmall + otherLarge

    # Return the total emissions from food
    return dietEmissions + eatingOutEmissions + wasteEmissions + petEmissions


def carbonEmissionTransport():
    """ Calculate the emissions from the transport section. """
    vehicle = request.form.get("transport_1")

    # Find the EF for the chosen vehicle and parameters
    if vehicle == "MOTORBIKE_EF":
        size = int(request.form.get("transport_1.1"))
        vehicleEF = const.MOTORBIKE_EF[size]
    elif vehicle == "CAR_EF":
        size = int(request.form.get("transport_1.1"))
        fuel = int(request.form.get("transport_1.2"))
        vehicleEF = const.CAR_EF[size][fuel]
    elif vehicle == "BUS_EF":
        vehicleEF = const.BUS_EF
    elif vehicle == "WALK_BIKE_EF":
        vehicleEF = const.WALK_BIKE_EF

    # Get the values from the form
    chosenMileage = float(request.form.get("transport_2"))
    trainMileage = float(request.form.get("transport_3"))
    domestic = float(request.form.get("transport_4_domestic")) * const.DOMESTIC_EF
    upto1250 = float(request.form.get("transport_4_1250")) * const.UPTO1250_EF
    upto2500 = float(request.form.get("transport_4_2500")) * const.UPTO2500_EF
    upto5500 = float(request.form.get("transport_4_5500")) * const.UPTO5500_EF
    upto9000 = float(request.form.get("transport_4_9000")) * const.UPTO9000_EF
    upto17500 = float(request.form.get("transport_4_17500")) * const.UPTO17500_EF

    # Calculate different emissions for the questions
    vehicleEmissions = vehicleEF * chosenMileage * const.YEAR_IN_WEEKS
    trainEmissions = const.TRAIN_EF * trainMileage * const.YEAR_IN_MONTHS
    flightEmissions = domestic + upto1250 + upto2500 + upto5500 + upto9000 + upto17500

    # Return the total emissions for transport
    return vehicleEmissions + trainEmissions + flightEmissions


def carbonEmissionPurchasing():
    """ Calculate the emissions from the purchasing section. """
    # Get the values from the form
    electricAppliance = float(request.form.get("purchasing_1"))
    clothing = float(request.form.get("purchasing_2"))
    chemical = float(request.form.get("purchasing_3"))
    goods = float(request.form.get("purchasing_4"))

    # Calculate different emissions for the questions
    electricApplianceEmissions = electricAppliance * const.ELECTRICAL_APPLIANCE_EF
    clothingEmissions = clothing * const.CLOTHING_EF * const.YEAR_IN_MONTHS
    chemicalEmissions = chemical * const.CHEMICAL_EF * const.YEAR_IN_MONTHS
    goodsEmissions = goods * const.OTHER_MANUF_EF * const.YEAR_IN_MONTHS

    # Return the total emissions for purchasing
    return electricApplianceEmissions + clothingEmissions + chemicalEmissions + goodsEmissions


def carbonEmissionEnergy():
    """ Calculate the emissions for the energy section. """
    # Get the values from the form
    people = int(request.form.get("energy_1"))
    house = int(request.form.get("energy_2"))
    heat = int(request.form.get("energy_3"))
    water = int(request.form.get("energy_4"))

    # Calculate different emissions for each question
    electricEmissions = (house/people) * const.ELECTRIC_EF
    heatEmissions = (heat/people) * const.HEAT_EF
    waterEmissions = water * const.WATER_EF * const.YEAR_IN_DAYS

    # Return the total emissions for energy
    return electricEmissions + heatEmissions + waterEmissions


def calcPercentage(total, part):
    """ Take two values and work out the percentage of one the other. """
    return (part/total) * 100


def results(totalEmissionTonne, foodPercent, transportPercent
            , purchasingPercent, energyPercent, trees, date, saved):
    """ Render the results page. """
    footprint = imageCreation(foodPercent, transportPercent, purchasingPercent)

    # Temporarily save the foot print and encode it into Bytes
    footprint.save('static/img/footprint.png')
    with open('static/img/footprint.png', "rb") as img_file:
        footprintByte = base64.b64encode(img_file.read())

    os.remove('static/img/footprint.png')

    return render_template('results.html', carbonFootprint=totalEmissionTonne
                           , foodPercent=foodPercent
                           , transportPercent=transportPercent
                           , purchasingPercent=purchasingPercent
                           , energyPercent=energyPercent
                           , footprint=footprintByte
                           , trees=trees
                           , date=date.strftime("%d/%m/%y")
                           , save=saved
                           , hasNav=True)


@calculator_blueprint.route('/save', methods=['POST'])
@login_required
def save():
    """ Save a users footprint data to the database. """
    # Get values to save
    emissions = float(request.form.get("totalEmissionsTonne"))
    food = int(request.form.get("foodPercent"))
    transport = int(request.form.get("transportPercent"))
    purchasing = int(request.form.get("purchasingPercent"))
    energy = int(request.form.get("energyPercent"))
    date = datetime.today()

    footprint = imageCreation(food, transport, purchasing)

    # Temporarily save the foot print and encode it into Bytes
    footprint.save('static/img/footprint.png')
    with open('static/img/footprint.png', "rb") as img_file:
        footprintByte = base64.b64encode(img_file.read())

    # Update database with new record
    new_footprint = SurveyResult(user_id=current_user.id
                                 , carbon_emissions=emissions
                                 , food=food
                                 , transport=transport
                                 , purchasing=purchasing
                                 , energy=energy
                                 , footprint=footprintByte
                                 , date=date)

    os.remove('static/img/footprint.png')
    db.session.add(new_footprint)
    db.session.commit()

    return results(emissions, food, transport, purchasing, energy, int(round(emissions/const.TREES, 0))
                   , date, False)


def imageCreation(food, transport, purchasing):
    """ Creates a footprint image with variable sized colour sections. """
    # Create an image of a footprint based on the users footprint makeup
    # Get all footprint images
    greenFoot = Image.open('static/img/green footprint.png')
    redFoot = Image.open('static/img/red footprint.png')
    blueFoot = Image.open('static/img/blue footprint.png')
    yellowFoot = Image.open('static/img/yellow footprint.png')
    footprint = Image.new('RGB', (greenFoot.width, greenFoot.height), "#b1dbf2")

    # Crop footprint images based on the percentages to determine the sections size
    greenFoot = greenFoot.crop((0, 0, greenFoot.width, (food / 100) * greenFoot.height))
    redFoot = redFoot.crop((0, (food / 100) * redFoot.height, redFoot.width, ((food + transport) / 100) * redFoot.height))
    blueFoot = blueFoot.crop((0, ((food + transport) / 100) * blueFoot.height, blueFoot.width, ((food + transport + purchasing) / 100) * blueFoot.height))
    yellowFoot = yellowFoot.crop((0, ((food + transport + purchasing) / 100) * yellowFoot.height, yellowFoot.width, yellowFoot.height))

    # Combine the individual sections into one image
    footprint.paste(greenFoot, (0, 0))
    footprint.paste(redFoot, (0, greenFoot.height))
    footprint.paste(blueFoot, (0, greenFoot.height + redFoot.height))
    footprint.paste(yellowFoot, (0, greenFoot.height + redFoot.height + blueFoot.height))

    return footprint
