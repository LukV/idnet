from flask import render_template, request, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_babel import gettext
from config import LANGUAGES

from app import babel, db
from app.auth.forms import LoginForm, SignupForm
from app.auth.models import User
from app.auth import auth

@auth.route('/', methods=["GET", "POST"])
@auth.route('/login', methods=["GET", "POST"])
@auth.route('/signin', methods=["GET", "POST"])
def login():
	# TODO translations
	# TODO remember_me

	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))

		flash(gettext('Invalid username or password.'))

 	return render_template('auth/login.html', 
		title=gettext('Log in'),
		form=form)

@auth.route('/signup', methods=["GET", "POST"])
def signup():

	form = SignupForm(request.form)

	if form.validate_on_submit():
		username = form.username.data
		email    = form.email.data
		password = form.password.data
		
		if not username:
			username = email.split('@')[0]
		
		user = User(username, email)
		user.password = password
		user.password_hash
		user.role = 2
		user.status = 1
		db.session.add(user)
		db.session.commit()
		
		flash(gettext('You can now login.'))
		return redirect(url_for('auth.login'))

	return render_template('auth/signup.html', 
		title=gettext('Sign up'),
		form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash(gettext('You have been logged out.'))
	return redirect(url_for('main.index'))
