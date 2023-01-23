from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import URL, DataRequired


class LinkForm(FlaskForm):
    """ This class is to validate the url that administrator inputted is correct. """

    link = StringField(validators=[DataRequired(), URL(message='* Invalid URL')])
    submit = SubmitField()


class FAQForm(FlaskForm):
    """ This is a form to review and append FAQs, and approve them for the webpage. """
    question = TextAreaField(validators=[DataRequired()])
    answer = TextAreaField(validators=[DataRequired()])
    approved = BooleanField()
    submit = SubmitField()


class linkForm(FlaskForm):
    """ This is a form to review and append links. """
    name = StringField(validators=[DataRequired()])
    link = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    submit = SubmitField()




