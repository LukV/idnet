import os

from flask import Flask, render_template
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import BASEDIR

app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)
db    = SQLAlchemy(app)
lm    = LoginManager()

lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

from app.main.controllers  import main  as main_module
from app.auth.controllers  import auth  as auth_module
from app.admin.controllers import admin as admin_module

# Register blueprint(s)
app.register_blueprint(main_module)
app.register_blueprint(auth_module)
app.register_blueprint(admin_module)

from auth import models
