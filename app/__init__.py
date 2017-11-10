import os

from flask import Flask, render_template
from flask_babel import Babel
from config import BASEDIR

app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_public.controllers import mod_public as public_module

# Register blueprint(s)
app.register_blueprint(public_module)
