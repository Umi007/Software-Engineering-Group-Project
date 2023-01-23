# Time constants
YEAR_IN_DAYS = 365
YEAR_IN_WEEKS = 52
YEAR_IN_MONTHS = 12

# Conversion
KG_TO_TON = 0.001

# UK government emissions
# kgCO2e/capita
UK_EMISSIONS = 2750

# Food emission factors
# (kgCO2e/day)
HIGH_MEAT_EF = 7.19
MEDIUM_MEAT_EF = 5.63
LOW_MEAT_EF = 4.67
PESCATARIAN_EF = 3.91
VEGETARIAN_EF = 3.81
VEGAN_EF = 2.89
# (kgCO2e/£)
EATING_OUT_EF = 0.4
# (kg) and (kgCO2e/kg)
FOOD_A_YEAR = 202.58
WASTE_EF = 2.54
# (kgCO2e/year)
FISH_EF = 25
CAT_EF = 310
SMALL_DOG_EF = 770
LARGE_DOG_EF = 2500
OTHER_SMALL = 167.5
OTHER_LARGE = 1635

# Transport emission factors
# (kgCO2e/mile) SMALL, MEDIUM, LARGE
MOTORBIKE_EF = [0.13, 0.16, 0.21]
# (kgCO2e/mile) DIESEL, PETROL, HYBRID, PI HYBRID, EV
# SMALL
# MEDIUM
# LARGE
CAR_EF = [[0.22, 0.24, 0.17, 0.04, 0]
          , [0.27, 0.30, 0.10, 0.11, 0]
          , [0.33, 0.45, 0.24, 0.12, 0]]
# (kgCO2e/mile)
BUS_EF = 0.06
WALK_BIKE_EF = 0
# (kgCO2e/passenger.mile)
TRAIN_EF = 0.02
DOMESTIC_EF = 109.61
UPTO1250_EF = 191.91
UPTO2500_EF = 383.83
UPTO5500_EF = 1062
UPTO9000_EF = 1737.81
UPTO17500_EF = 3379.08

# Purchasing emission factors
# (kgCO2e/£)
ELECTRICAL_APPLIANCE_EF = 0.62
CLOTHING_EF = 0.68
CHEMICAL_EF = 0.9
OTHER_MANUF_EF = 0.45

# Energy emission factors
# (kwh/year)
MID_TERRACE = 2779
FLAT = 2829
END_TERRACE = 3442
SEMI_DETACHED = 3847
BUNGALOW = 3866
DETACHED = 4153
LOW_HEAT = 8000
MEDIUM_HEAT = 12000
HIGH_HEAT = 17000
# (kgCO2e/kwh)
ELECTRIC_EF = 0.21
HEAT_EF = 0.18
# (kgCO2e/litre)
WATER_EF = 0.000421

# Tree calculation
TREES = 0.02
