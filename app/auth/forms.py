from app import babel
from app.auth.models import User
from flask_babel import gettext
from config import LANGUAGES
from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, ValidationError
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
	email = StringField(gettext('Email Address'), [
		Email(), 
		Required(message=gettext('E-mail is required to login.')), 
		Length(1, 128)])
	password = PasswordField(gettext('Password'), [
		Required(message=gettext('Must provide a password. ;-)'))])	
	remember_me = BooleanField('remember_me', default=False)
	
class SignupForm(Form):
	username  = StringField(gettext('First name'))
	email     = StringField(gettext('Email address'), [
		Email(), 
		Required(), 
		Length(1, 128)])
	password  = PasswordField(gettext('Password'), [
		Required()])

	'''
	When a form defines a method with the prefix validate_ 
	followed by the name of a field, the method
	is invoked in addition to any regularly defined validators.
	'''
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError(gettext('Email already exists. Try logging in.'))
