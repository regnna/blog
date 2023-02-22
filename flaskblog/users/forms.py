
# users/ forms. py
from flask_wtf import FlaskForm
from flask_wtf. file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog. models import User


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')


    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken, Please choose a different username.')


    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already taken, Please choose a different Email or consider login')


class LoginForm(FlaskForm):
    # username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    # confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    # password=PasswordField('Password',validators=[DataRequired()])
    # confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    picture=FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is taken, Please choose a different username.')

    def validate_email(self,email):
        if email.data!=current_user.email:
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email is already taken, Please choose a different Email or consider login')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        # if email.data!=current_user.email:
        email=User.query.filter_by(email=email.data).first()
        if email is None:
            raise ValidationError('There is no account with this email, register with it first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')