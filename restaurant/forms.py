from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label = 'username', validators = [Length(min = 2, max = 30), DataRequired()])
    email_address = StringField(label = 'email', validators = [Email(), DataRequired()])
    password1 = PasswordField(label = 'password1', validators = [Length(min = 6), DataRequired()])
    password2 = PasswordField(label = 'password2', validators = [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label = 'username', validators = [DataRequired()])
    password = PasswordField(label = 'password', validators = [DataRequired()])
    submit = SubmitField(label = 'Sign In')

class OrderIDForm(FlaskForm):
    orderid = StringField(label ='order-id', validators = [Length(min = 10), DataRequired()])      
    submit = SubmitField(label = 'Track')

class ReserveForm(FlaskForm):
    submit = SubmitField(label = 'Reserve')

class OrderForm(FlaskForm):
    submit = SubmitField()