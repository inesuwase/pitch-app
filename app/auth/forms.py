from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):

    email = StringField('Your Email',validators=[Required(),Email()])
    username = StringField('Enter username',validators = [Required()])
    password = PasswordField('Enter Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is a person with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('There is a person with that username ')


class LoginForm(FlaskForm):
    email = StringField('Your Email ',validators=[Required(),Email()])
    password = PasswordField('Enter Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')