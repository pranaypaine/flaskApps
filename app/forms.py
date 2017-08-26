from wtforms import *

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
	])
	confirm = PasswordField('Confirm Password')

class LoginForm(Form):
	"""docstring for LoginForm"""
	username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
	password = PasswordField('Password', [validators.DataRequired()])
	def __init__(self, arg):
		super(LoginForm, self).__init__()
		self.arg = arg
		