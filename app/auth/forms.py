from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email,length


class RegistrationForm(FlaskForm):
    email = StringField('Please enter your email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Create Password', validators=[DataRequired(), length(min=4)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    password = PasswordField('Your Password', validators=[DataRequired()])
    submit = SubmitField('Login')