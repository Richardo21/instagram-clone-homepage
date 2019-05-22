from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField, validators
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
	email = StringField(validators = [DataRequired])
	fullname = TextField(validators = [DataRequired])
	username = StringField(validators = [DataRequired])
	password = PasswordField(validators = [DataRequired])