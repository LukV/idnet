from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import lm

class Base(db.Model):

	__abstract__  = True

	id            = db.Column(db.Integer,  primary_key=True)
	date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
								onupdate=db.func.current_timestamp())

class User(UserMixin, Base):

	__tablename__ = 'auth_user'

	username      = db.Column(db.String(128), nullable=False)
	email         = db.Column(db.String(128), nullable=False, unique=True, index=True)
	password_hash = db.Column(db.String(128), nullable=False)

	role     = db.Column(db.SmallInteger, nullable=True)
	status   = db.Column(db.SmallInteger, nullable=True)

	def __init__(self, username, email):
		self.username = username
		self.email    = email

	def __repr__(self):
		return '<User %r>' % (self.username)  

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
		
		
	@lm.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
