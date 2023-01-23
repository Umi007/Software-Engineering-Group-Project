from flask import Blueprint, render_template, request, session
from flask_login import current_user
from models import QuizResult
from app import db

# Config
quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates')


@quiz_blueprint.route('/quiz')
def quiz():
    """ This function is to view the quiz home page. """
    return render_template('quiz-home.html', hasNav=True)


@quiz_blueprint.route('/quiz_questions_general')
def quiz_questions_general():
    """ This function is to view the quiz questions general page. """
    return render_template('quiz_questions_general.html', hasNav=False)


@quiz_blueprint.route('/quiz_questions_advanced')
def quiz_questions_advanced():
    """ This function is to view the quiz questions advanced page. """
    return render_template('quiz_questions_advanced.html', hasNav=False)


@quiz_blueprint.route('/general', methods=['POST'])
def count_general_quiz():
    """ This function is to calculate the overall score for the general quiz. """

    score = 0
    sample_general_answer = "11111DBADE"
    user_answer = ""
    # get user's answers from form
    for i in range(1, 11):
        user_answer += request.form.get("choice" + str(i))
    for j in range(len(sample_general_answer)):
        if user_answer[j] == sample_general_answer[j]:
            score += 1

    session['general_quiz_answer'] = user_answer
    session['general_quiz_score'] = score

    if current_user.is_authenticated:
        new_quiz_result = QuizResult(user_id=current_user.id,
                                     user_answer=user_answer,
                                     user_mark=score,
                                     quiz_category="general")
        db.session.add(new_quiz_result)
        db.session.commit()

    return render_template("quiz_result.html", quiz_score=score, hasNav=True)


@quiz_blueprint.route('/advance', methods=['POST'])
def count_advance_quiz():
    """ This function is to calculate the overall score for the advance quiz. """
    score = 0
    sample_advance_answer = "00011CCCCB"
    user_answer = ""
    # get user's answers from form
    for i in range(11, 21):
        user_answer += request.form.get("choice" + str(i))
    for j in range(len(sample_advance_answer)):
        if user_answer[j] == sample_advance_answer[j]:
            score += 1

    session['advance_quiz_answer'] = user_answer
    session['advance_quiz_score'] = score
    if current_user.is_authenticated:
        new_quiz_result = QuizResult(user_id=current_user.id,
                                     user_answer=user_answer,
                                     user_mark=score,
                                     quiz_category="advance")
        db.session.add(new_quiz_result)
        db.session.commit()
    return render_template("quiz_result.html", quiz_score=score, hasNav=True)


