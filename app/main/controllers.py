from app import babel
from flask import Blueprint, render_template, request, g, redirect, url_for
from flask_login import login_required
from flask_babel import gettext
from config import LANGUAGES
from app.main import main

@babel.localeselector
def get_locale():
	return request.accept_languages.best_match(LANGUAGES.keys())

@main.route('/')
@main.route('index')
def index():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('main.dashboard'))

	return render_template('main/index.html', 
		title=gettext('Home'))

@main.route('privacy-policy')
def privacy():
	return render_template('main/privacy.html', 
		title=gettext('Privacy Policy'))

@main.route('dashboard')
@login_required
def dashboard():
	return render_template('main/dashboard.html', 
		title=gettext('Dashboard'))

@main.route('controllers')
@login_required
def controllers():
	return render_template('main/controllers.html', 
		title=gettext('Controllers'))
