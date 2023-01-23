from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class CreatePost(FlaskForm):
    """ Form for submitting a post. """
    submit_button = SubmitField()


class CreateComment(FlaskForm):
    """ Form for creating and adding a comment. """
    comment = StringField(Length(min=0, max=200, message="Comments can't exceed 200 characters"))
    submit_button = SubmitField()


class SearchFriend(FlaskForm):
    """ Form for submitting a friend search. """
    submit_button = SubmitField()
