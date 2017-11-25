from app import babel
from flask import Blueprint, render_template, request
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
	return render_template('main/index.html', 
		title=gettext('Home'))

@main.route('secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!'
