import re
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError


def special_char_check(form, field):
    """ Check the special characters in input. """
    exclude_chars = "/?.>,<;:|\]}[{=+-_)(*&^%$#@!`~'"
    for char in field.data:
        if char == " ":
            raise ValidationError('* Space is not allowed.')
        if char in exclude_chars:
            raise ValidationError(f'* Character {char} is not allowed.')


class RegisterForm(FlaskForm):
    """ Form for registering a new user. """
    email = StringField(validators=[InputRequired(), Email(message='* Invalid email address')])
    security_code = StringField()
    firstname = StringField(validators=[InputRequired(), special_char_check])
    surname = StringField(validators=[InputRequired(), special_char_check])
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=12,
                                                                 message='* Password should be between '
                                                                         '6 to 12 characters length.')])
    password_confirmation = PasswordField(
        validators=[InputRequired(),
                    EqualTo('password',
                            message='* Passwords did not match. '
                                    'Please try again.')])
    # Submit register form
    sign_up = SubmitField('Sign Up')
    recaptcha = RecaptchaField()
    # password validation
    def validate_password(self, password):
        """This method is to validate password."""

        password_format = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)')
        if not password_format.match(self.password.data):
            raise ValidationError('* Password must include least 1 uppercase, '
                                  '1 lowercase, 1 digit and 1 special character.')

    # security code validation
    def validate_security_code(self, security_code):
        """ This method is to validate a security code. """
        if self.security_code.data is None or len(self.security_code.data) == 0:
            pass
        else:
            security_code_format = re.compile(r'(?=[0-9][0-9][0-9][0-9][0-9][0-9])')
            if not security_code_format.match(self.security_code.data):
                raise ValidationError('* Code should be 6 digits length')


class UpdateProfile(FlaskForm):
    """ Form to update a profile"""
    username = StringField(validators=[InputRequired(), special_char_check])
    firstname = StringField(validators=[InputRequired(), special_char_check])
    surname = StringField(validators=[InputRequired(), special_char_check])
    submit_button = SubmitField()


class UpdateProfilePassword(FlaskForm):
    """ Form to update a users password. """
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=12,
                                                                 message='* Password should be between '
                                                                         '6 to 12 characters length.')])
    password_confirmation = PasswordField(
        validators=[InputRequired(),
                    EqualTo('password',
                            message='* Passwords did not match. '
                                    'Please try again.')])

    submit_button = SubmitField()



class LoginForm(FlaskForm):
    """ Form for users to log in. """
    email = StringField(validators=[InputRequired(), Email()])
    security_code = StringField()
    password = PasswordField(validators=[InputRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField()

    # security code validation
    def validate_security_code(self, security_code):
        """ This method is to validate a security code. """
        if self.security_code.data is None or len(self.security_code.data) == 0:
            pass
        else:
            security_code_format = re.compile(r'(?=[0-9][0-9][0-9][0-9][0-9][0-9])')
            if not security_code_format.match(self.security_code.data):
                raise ValidationError('* Code should be 6 digits length')
