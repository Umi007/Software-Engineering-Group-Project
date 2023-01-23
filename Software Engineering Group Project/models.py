import base64
import os.path

from datetime import datetime
from flask_login import UserMixin
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from werkzeug.security import generate_password_hash

from app import db


class User(db.Model, UserMixin):
    """ This user class is to set a table for storing users' account and set the relations to other tables. """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Authentication information of user
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    pin_key = db.Column(db.String(100), nullable=False)

    # User information
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.String(100), nullable=False, default='user')
    profile_picture = db.Column(db.BLOB, nullable=False)

    # Activity information of login user
    register_date = db.Column(db.DateTime, nullable=False)
    last_logged_date = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)

    background = db.Column(db.BLOB, nullable=True)
    accountCover = db.Column(db.BLOB, nullable=True)

    def __init__(self, email, firstname, surname, username, password, role, profile_picture):
        self.email = email
        self.firstname = firstname
        self.surname = surname
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role
        self.profile_picture = profile_picture
        self.pin_key = base64.urlsafe_b64encode(
            scrypt(password, str(get_random_bytes(32)), 32, N=2 ** 14, r=8, p=1))
        self.register_date = datetime.now()
        self.last_logged_date = None
        self.current_logged_in = None
        self.background = None
        self.accountCover = None


class SurveyResult(db.Model):
    __tablename__ = 'surveyResult'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    carbon_emissions = db.Column(db.Float, nullable=False)
    food = db.Column(db.Integer, nullable=False)
    transport = db.Column(db.Integer, nullable=False)
    purchasing = db.Column(db.Integer, nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    footprint = db.Column(db.BLOB, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, carbon_emissions, food, transport, purchasing, energy, footprint, date):
        self.user_id = user_id
        self.carbon_emissions = carbon_emissions
        self.food = food
        self.transport = transport
        self.purchasing = purchasing
        self.energy = energy
        self.footprint = footprint
        self.date = date


class QuizQuestions(db.Model):
    """ This quiz questions class is to set a table in the database."""
    __tablename__ = 'quizQuestions'

    id = db.Column(db.Integer, primary_key=True)

    # Quiz questions information
    question = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(500), nullable=False)
    options = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(100), nullable=False)

    def __init__(self, question, category, options, description, source, answer):
        self.question = question
        self.category = category
        self.options = options
        self.description = description
        self.source = source
        self.answer = answer


class QuizResult(db.Model):
    """ This quiz result class is to set a table to store the result of quiz taken by users."""
    __tablename__ = 'quizResult'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user_answer = db.Column(db.Text, nullable=False)
    user_mark = db.Column(db.Integer, nullable=False)
    quiz_category = db.Column(db.String(100),nullable=False)

    def __init__(self, user_id, user_answer, user_mark, quiz_category):
        self.user_id = user_id
        self.user_answer = user_answer
        self.user_mark = user_mark
        self.quiz_category = quiz_category

class UserFriends(db.Model):
    """
    This users friends class is to set a table to store the
    many to many relationship between users.

    """
    __tablename__ = 'UserFriends'

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user2_id = db.Column(db.Integer, nullable=False)
    starredFriend = db.Column(db.Boolean, nullable=True)

    users = db.relationship('User', overlaps="user_friends")

    def __init__(self, user1_id, user2_id, starredFriend):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.starredFriend = starredFriend


class SocialPosts(db.Model):
    __tablename__ = 'SocialPosts'
    PostId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    PostText = db.Column(db.Text, nullable=True)
    PostImg = db.Column(db.BLOB, nullable=True)
    PostDate = db.Column(db.String(10), nullable=True)

    def __init__(self, UserId, PostText, PostImg):
        self.UserId = UserId
        self.PostText = PostText
        self.PostImg = PostImg
        self.PostDate = "{} {}".format(datetime.now().day , datetime.now().strftime("%B"))


class SocialPostLikes(db.Model):
    __tablename__ = 'SocialPostLikes'
    LikeId = db.Column(db.Integer, primary_key=True)
    PostId = db.Column(db.Integer, db.ForeignKey(SocialPosts.PostId), nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    SocialPosts = db.relationship('SocialPosts')
    # users = db.relationship('User')

    def __init__(self, PostId, UserId):
        self.PostId = PostId
        self.UserId = UserId


class SocialPostComments(db.Model):
    __tablename__ = 'SocialPostComments'
    CommentsId = db.Column(db.Integer, primary_key=True)
    PostId = db.Column(db.Integer, db.ForeignKey(SocialPosts.PostId), nullable=False)
    CommentText = db.Column(db.Text, nullable=True)
    UserId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    SocialPosts = db.relationship('SocialPosts')
    users = db.relationship('User')

    def __init__(self, PostId, CommentText, UserId):
        self.PostId = PostId
        self.CommentText = CommentText
        self.UserId = UserId


class FAQ(db.Model):
    __tablename__ = 'FAQ'
    FAQID = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(500), nullable=True)
    approved = db.Column(db.Boolean, nullable=False)

    def __init__(self, question, answer, approved):
        self.question = question
        self.answer = answer
        self.approved = approved

    def update(self, question, answer, approved):
        self.question = question
        self.answer = answer
        self.approved = approved
        db.session.commit()


class UsefulLinks(db.Model):
    __tablename__ = 'UsefulLinks'
    linkID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, link, description):
        self.name = name
        self.link = link
        self.description = description

    def update(self, name, link, description):
        self.name = name
        self.link = link
        self.description = description
        db.session.commit()


class ReportedUser(db.Model):
    __tablename__ = 'ReportedUser'

    reportedUserId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    users = db.relationship('User')

    def __init__(self, UserId):
        self.UserId = UserId


class ReportedPost(db.Model):
    __tablename__ = 'ReportedPost'

    reportedUserId = db.Column(db.Integer, primary_key=True)
    PostId = db.Column(db.Integer, db.ForeignKey(SocialPosts.PostId), nullable=False)

    SocialPosts = db.relationship('SocialPosts')

    def __init__(self, PostId):
        self.PostId = PostId


def init_db():
    """Initialised the database and input value"""

    db.drop_all()
    db.create_all()

    # Import the admin test accounts from csv file
    if os.path.exists('Resources/admin_accounts.csv'):
        from Resources.auto_import import AutoImport
        admin_accounts = AutoImport().auto_import('admin_accounts.csv')
        for account in admin_accounts:
            db.session.add(account)

    # Import the quiz questions from csv file
    if os.path.exists('Resources/quizQuestions.csv'):
        from Resources.auto_import import AutoImport
        quiz_questions = AutoImport().auto_import('quizQuestions.csv')
        for questions in quiz_questions:
            db.session.add(questions)

    # Import the links from csv file
    if os.path.exists('Resources/links.csv'):
        from Resources.auto_import import AutoImport
        links = AutoImport().auto_import('links.csv')
        for link in links:
            db.session.add(link)

    # Import the FAQs from csv file
    if os.path.exists('Resources/FAQ.csv'):
        from Resources.auto_import import AutoImport
        FAQs = AutoImport().auto_import('FAQ.csv')
        for faq in FAQs:
            db.session.add(faq)

    test_user = User.query.filter_by(role='admin').first()
    post1 = SocialPosts(
        UserId=test_user.id,
        PostText="Helllooooo",
        PostImg=None
    )
    db.session.add(post1)
    post2 = SocialPosts(
        UserId=test_user.id,
        PostText="Kaleeemm ",
        PostImg=None
    )
    db.session.add(post2)

    post = SocialPosts.query.filter_by(UserId=test_user.id).all()

    postLikes1 = SocialPostLikes(
        PostId=post[0].PostId,
        UserId=test_user.id
    )
    db.session.add(postLikes1)

    postLikes2 = SocialPostComments(
        PostId=post[1].PostId,
        CommentText="Well done!!",
        UserId=test_user.id
    )
    db.session.add(postLikes2)
    db.session.commit()
