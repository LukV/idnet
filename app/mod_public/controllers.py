from app import babel
from flask import Blueprint, render_template
from flask_babel import gettext
from config import LANGUAGES

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_public = Blueprint('public', __name__, url_prefix='/public')

@babel.localeselector
def get_locale():
	return request.accept_languages.best_match(LANGUAGES.keys())

@mod_public.route('/')
@mod_public.route('/index')
def index():
	return render_template('public/index.html', 
		title=gettext('Home'))
