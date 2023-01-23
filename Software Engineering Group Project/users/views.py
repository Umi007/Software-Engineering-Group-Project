import logging
import base64
import random
from werkzeug.utils import secure_filename
from Resources.verification import Verification
from datetime import datetime
from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, SocialPosts, SocialPostLikes, SocialPostComments, QuizResult, UserFriends,SurveyResult
from flask_login import login_user, login_required, current_user, logout_user
from users.forms import RegisterForm, LoginForm, UpdateProfile, UpdateProfilePassword
from app import db
import os

# CONFIG
users_blueprint = Blueprint('users', __name__, template_folder='templates')


# View registration
@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    This function is to get the user register information from web and

    store into database.

    """
    # Create a new form object
    form = RegisterForm()

    # POST method is requested
    if form.validate_on_submit():
        user_in_db = User.query.filter_by(email=form.email.data).first()

        if user_in_db:
            flash('Email address already registered')

            # If the email address is signed in
            return render_template('register.html', form=form, hasNav=True)

        # Create a verify session for a registering user
        if session.get('verify') is None:
            verify = Verification(form.email.data, 'register')
            code = verify.send_code()
            session['sent'] = True
            session['email'] = form.email.data
            session['verify'] = str(code)

            # Show succeeded sending message to user
            flash("An email is sent to your email. "
                  "Please enter the security code to verify your email address!")
            return render_template('register.html', form=form, hasNav=True)

        elif form.email.data != session.get('email'):

            # If user reenter an new email
            verify = Verification(form.email.data, 'register')
            code = verify.send_code()
            session['email'] = form.email.data
            session['verify'] = str(code)

            # Show succeed sending message to user
            flash("An email is resent to your email. "
                  "Please enter the security code to verify your email address!")
            return render_template('register.html', form=form, hasNav=True)

        # Generate username for user
        if User.query.filter_by(username=form.firstname.data + form.surname.data).first():
            username = form.firstname.data + form.surname.data + str(random.randint(1, 100))
        else:
            username = form.firstname.data + form.surname.data

        # Generate default profile picture
        img_file = open("static/img/profile-picture.png", "rb")
        profile_img = base64.b64encode(img_file.read())
        img_file.close()

        if session.get('verify') is not None and form.security_code.data == session.get('verify'):
            # Using the form data to create a new user
            new_user = User(email=form.email.data,
                            firstname=form.firstname.data,
                            surname=form.surname.data,
                            username=username,
                            password=form.password.data,
                            role='user',
                            profile_picture=profile_img)

            # Add the user to database
            db.session.add(new_user)
            db.session.commit()
            session.pop('verify', None)
            session.pop('sent', False)

            # auto sign in the new user
            user = User.query.filter_by(email=form.email.data).first()
            sign_in(user)

            # Update register operation to logging
            logging.warning('SECURITY - User registration [%s, %s]', form.email.data, request.remote_addr)
            return redirect(url_for('users.profile'))

        elif (form.security_code.data is None or len(form.security_code.data) == 0) and \
                session.get('verify') is not None and session.get('sent'):
            flash('Please verify your email address')
            return render_template('register.html', form=form, hasNav=True)

        elif (form.security_code.data is not None or len(form.security_code.data) != 0) and \
                form.security_code.data != session.get('verify') and session.get('sent'):
            flash('Incorrect security code. Please try again.')
            return render_template('register.html', form=form, hasNav=True)

    # If GET method is requested or form is not valid back to same page
    return render_template('register.html', form=form, hasNav=True)


@users_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """ Get all data for profile page and render it. """
    accFriend=[]
    userF = UserFriends.query.filter(UserFriends.user1_id == current_user.id).limit(6).all()
    userF1 = UserFriends.query.filter(UserFriends.user2_id == current_user.id).limit(6).all()
    cFootprint = SurveyResult.query.filter_by(user_id=current_user.id).all()
    quizResult = QuizResult.query.filter_by(user_id=current_user.id).all()

    friends = userF + userF1

    if friends:
        for friend in friends:
            if friend.user1_id == current_user.id:
                accFriend.append(User.query.filter_by(id=friend.user2_id).first())
            else:
                accFriend.append(User.query.filter_by(id=friend.user1_id).first())

    pastFootprints = []
    currentFootprint = None
    if cFootprint:
        currentFootprint = cFootprint[0]
        for footprint in cFootprint:
            if currentFootprint.date > footprint.date:
                currentFootprint=footprint
            else:
                pastFootprints.append(footprint)



    form = UpdateProfile()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Confirm':

            if form.validate_on_submit():
                user = User.query.filter(User.id == current_user.id).first()
                user.username = form.username.data
                user.firstname = form.firstname.data
                user.surname = form.surname.data
                if request.files['userProfilePic']:
                    pic = request.files['userProfilePic']
                    pic.save(os.path.join('static/images', secure_filename(pic.filename)))
                    with open('static/images/' + pic.filename, "rb") as img_file:
                        profile_img = base64.b64encode(img_file.read())
                    user.profile_picture = profile_img
                    os.remove('static/images/' + pic.filename)

                if request.files['userprofileBackground']:
                    pic = request.files['userprofileBackground']
                    pic.save(os.path.join('static/images', secure_filename(pic.filename)))
                    with open('static/images/' + pic.filename, "rb") as img_file:
                        background_img = base64.b64encode(img_file.read())
                    user.background = background_img
                    os.remove('static/images/' + pic.filename)

                db.session.commit()

                flash("Username has been updated")
                return redirect(url_for('users.profile'))

        elif request.form['submit_button'] == 'Delete Profile':
            User.query.filter_by(id=current_user.id).delete()
            SocialPosts.query.filter_by(UserId=current_user.id).delete()
            SocialPostLikes.query.filter_by(UserId=current_user.id).delete()
            SocialPostComments.query.filter_by(UserId=current_user.id).delete()
            db.session.commit()
            return logout()

        if request.form['submit_button'] == 'Click to Change':
            return redirect(url_for('users.profileChangePassword'))
        else:
            pass

    return render_template('profile.html', form=form, friends=accFriend
                           , quizResult=quizResult, currentFootprint=currentFootprint
                           , pastFootprint=pastFootprints, hasNav=True)


@users_blueprint.route('/profileChangePassword', methods=['GET', 'POST'])
@login_required
def profileChangePassword():
    """ Update a users password. """
    form = UpdateProfilePassword()
    if form.validate_on_submit():
        user = User.query.filter(User.id == current_user.id).first()
        user.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash('Password Updated')
        return redirect(url_for('users.profile'))

    return render_template('profileChangePassword.html', form=form, hasNav=True)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """ Verify user details and sign them in. """

    # Check login attempts
    if not session.get('logins'):
        session['logins'] = 0

    elif session.get('logins') >= 3:
        flash('Number of incorrect logins exceeded')

    form = LoginForm()

    if form.validate_on_submit():

        session['logins'] += 1
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):

            # Show remaining login attempts
            if session['logins'] == 3:
                flash('Number of incorrect logins exceeded')
            elif session['logins'] == 2:
                flash('Please check your login details and try again. 1 login attempt remaining')
            else:
                flash('Please check your login details and try again. 2 login attempts remaining')

            # Record the invalid login attempt to logging
            logging.warning('SECURITY - Invalid login attempt [%s]', request.remote_addr)

            return render_template('login.html', form=form, hasNav=True)

        # If not security code sent
        if not session.get('sent'):
            verify = Verification(form.email.data, 'login')
            code = verify.send_code()
            session['logins'] = session.get('logins') - 1
            session['sent'] = True
            session['verify'] = str(code)
            flash("A security code is sent to your email. "
                  "Please enter the security code to verify your email address!")
            return render_template('login.html', form=form, hasNav=True)

        # If user did not enter the code
        elif session.get('sent') and (form.security_code.data is None or len(form.security_code.data) == 0):
            session['logins'] = session.get('logins') - 1
            flash('Please verify your email address')
            return render_template('login.html', form=form, hasNav=True)

        # If the code is incorrect
        elif form.security_code.data is not None and session.get('verify') != form.security_code.data:
            session['logins'] = session.get('logins') - 1
            flash('Incorrect security code. Please try again.')
            return render_template('login.html', form=form)

        else:
            session['logins'] = 0
            session.pop('verify', None)
            session.pop('sent', False)
            # Call sign_in method to login user in server
            sign_in(user)

            # Updated login operation to logging
            logging.warning('SECURITY - User login [%s, %s, %s]',
                            current_user.id,
                            current_user.email,
                            request.remote_addr)

            # Check whether user have taken quizzes before login
            store_session_quiz(user)

            return redirect(url_for('users.profile'))

    return render_template('login.html', form=form, hasNav=True)


@users_blueprint.route('/logout')
def logout():
    """ Sign the user out and clear the session. """

    # Add internal server error handling
    try:
        current_user.id
    except Exception:
        return render_template('500.html')
    else:
        # Update logout operation to logging
        logging.warning('SECURITY - Log out [%s, %s, %s]',
                        current_user.id,
                        current_user.email,
                        request.remote_addr)

        logout_user()
        session.clear()
        return redirect(url_for('index'))


@login_required
@users_blueprint.route('/delFriend', methods=('GET', 'POST'))
def delFriend():
    f2 = UserFriends.query.filter_by(user1_id=request.form['removeFriend'],user2_id=current_user.id).first()
    f1 = UserFriends.query.filter_by(user2_id=request.form['removeFriend'],user1_id=current_user.id).first()

    if f1:
        UserFriends.query.filter_by(id=f1.id).delete()
    if f2:
        UserFriends.query.filter_by(id=f2.id).delete()
    db.session.commit()

    return redirect(url_for('users.profile'))


def store_session_quiz(user):
    """
    This method is to check the session have user quiz score.
    If it has, automatically store into database.
    """
    if session.get('general_quiz_score'):
        new_quiz_score = QuizResult(user_id=user.id,
                                    user_answer=session.get('general_quiz_answer'),
                                    user_mark=session.get('general_quiz_score'),
                                    quiz_category='general')
        db.session.add(new_quiz_score)
        db.session.commit()
        session.pop('general_quiz_score', None)

    if session.get('advance_quiz_score'):
        new_quiz_score = QuizResult(user_id=user.id,
                                    user_answer=session.get('advance_quiz_answer'),
                                    user_mark=session.get('advance_quiz_score'),
                                    quiz_category='advance')
        db.session.add(new_quiz_score)
        db.session.commit()
        session.pop('advance_quiz_score', None)


def sign_in(user):
    """
    This method is used to sign in user in the website system.
    """
    login_user(user)
    user.last_logged_date = user.current_logged_in
    user.current_logged_in = datetime.now()
    db.session.add(user)
    db.session.commit()