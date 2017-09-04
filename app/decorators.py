from functools import wraps
from flask import g, request, redirect, url_for, session, flash

def login_required(f):
	@wraps(f)
	def login_is_required(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You are not loggedin please login to view the page', 'danger')
			return redirect(url_for('login'))
	return login_is_required

def is_loggedin(f):
	@wraps(f)
	def already_loggedin(*args, **kwargs):
		if 'logged_in' in session:
			return redirect(url_for('dashboard'))
			
	return already_loggedin