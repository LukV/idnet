# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))  

LANGUAGES = {
	'en': 'English',
	'nl': 'Nederlands'
}

WTF_CSRF_ENABLED = True
SECRET_KEY = '7aT9QJnb79KFpYeLnrRfdw9dNVZ589Tc'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
