from flask import Blueprint, render_template, request
from flask_login import current_user
from app import db
from models import FAQ, UsefulLinks, User, SurveyResult, UserFriends
from sqlalchemy import or_

# Config
information_blueprint = Blueprint('information', __name__, template_folder='templates')


@information_blueprint.route('/reduce')
def reduce():
    """ Render the reduce page. """
    return render_template('reduce.html', hasNav=True)


@information_blueprint.route('/FAQ')
def loadFAQ():
    """ Render FAQ page with all FAQs stored in database. """
    # Only shows FAQs that have been approved
    questionAndAnswer = FAQ.query.filter_by(approved=1).all()

    return render_template('FAQ.html', FAQ=questionAndAnswer, hasNav=True)


@information_blueprint.route('/FAQsubmit', methods=["POST"])
def FAQsubmit():
    """ Get inputted question and add it to database. """
    questionAndAnswer = []
    try:
        questionAndAnswer = FAQ.query.filter_by(approved=1).all()
    except():
        pass
    question = request.form.get("FAQQuestion")

    questionToSubmit = FAQ(question=question, answer="", approved=0)
    db.session.add(questionToSubmit)
    db.session.commit()


    return render_template('FAQ.html', FAQ=questionAndAnswer, hasNav=True)


@information_blueprint.route('/usefulLinks')
def usefulLinks():
    """ Render the useful links page with all links stored in the database."""
    links = UsefulLinks.query.all()

    return render_template('usefulLinks.html', links=links, hasNav=True)


@information_blueprint.route('/leaderboard')
def leaderboard():
    """ Render the leaderboard page. """
    return render_template('leaderboard.html', hasNav=True)


@information_blueprint.route('/worldLeaderboard', methods=['POST'])
def worldLeaderboard():
    """ Find out the 10 users with the lowest current footprint out of all users. """
    leaders = []
    # Get all users
    users = User.query.all()
    # For each user get a list of all their recorded footprints
    for user in users:
        footprints = SurveyResult.query.filter_by(user_id=user.id).all()
        if len(footprints) > 0:
            # Find the most recent footprint and add it to leaders along with the user
            leaders.append((user, mostRecentFootprint(footprints)))

    # Sort all footprints
    insertionSortFootprint(leaders)

    return render_template('leaderboard.html', leaders=leaders[:10], type="WORLD", hasNav=True)


@information_blueprint.route('/friendLeaderboard', methods=['POST'])
def friendLeaderboard():
    """ Find out the 10 users with the lowest current footprint out of your friends. """
    leaders = []
    users = set()
    # Get all friend records
    records = UserFriends.query.filter(or_(UserFriends.user1_id == current_user.id
                                           , UserFriends.user2_id == current_user.id)).all()

    # Add both ideas to a set so there is no duplicates
    if len(records) > 0:
        for record in records:
            users.add(User.query.filter_by(id=record.user1_id).first())
            users.add(User.query.filter_by(id=record.user2_id).first())

    # Turn set into a list so it can be amended
    users = list(users)

    # Get all of a users footprints
    for user in users:
        footprints = SurveyResult.query.filter_by(user_id=user.id).all()
        if len(footprints) > 0:
            # # Find the most recent footprint and add it to leaders along with the user
            leaders.append((user, mostRecentFootprint(footprints)))

    # Sort all footprints
    insertionSortFootprint(leaders)

    return render_template('leaderboard.html', leaders=leaders, type="FRIENDS",hasNav=True)


def mostRecentFootprint(list):
    """ Find which footprint is the most recent and return it. """
    # Set most recent data and date object
    recentEmissions = list[0].date
    recent = list[0]

    for i in range(0, len(list)):
        # Compare date
        if list[i].date < recentEmissions:
            # If more recent amend most recent date and date object
            recentEmissions = list[i].date
            recent = list[i]

    return recent


def insertionSortFootprint(list):
    """ Insertion sort based on carbon equivelents, but sorts tuple order for leaderboard. """
    for i in range(1, len(list)):
        # Set the item (tuple) in the list, but also need the key value (float) which is the
        # amount of carbon equivalents of each footprint
        item = list[i]
        key = list[i][1].carbon_emissions
        j = i

        # Make sure to check against carbon equivalents not object
        while j > 0 and key < list[j-1][1].carbon_emissions:
            list[j] = list[j-1]
            j = j-1

        # Move items around
        list[j] = item
