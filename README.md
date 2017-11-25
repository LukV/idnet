# idnet

idnet is a typical web application, based on the Python microframework Flask. idnet's aim is to put the GDPR to work. Users can upload their personal data from Google, Facebook etc to idnet which then vizualizes the data and how it is used.

## Installation

### Set up Python, pip and virtualenv
Make sure to have python 3.6 and install additional packages:
* python-dev (development tools)
* pip (to manage packages)
* virtualenv

```
$ mkdir idnet
$ cd idnet
$ virtualenv -p /usr/bin/python3.6 env
```

### Start virtualenvironment
```
$ source env/bin/activate
```

### Install packages
```
$ pip install flask
$ pip install flask-babel
$ pip install flask-sqlalchemy
$ pip install sqlalchemy-migrate
$ pip install flask-wtf
$ pip install flask-login
```

### Freeze current state
```
$ pip freeze > requirements.txt
```

See the list of installed packages without the requirements format using “pip list”. Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

```
$ pip install -r requirements.txt
```

### Download source code
```
$ git clone https://github.com/LukV/idnet.git
```

### Create database

```
$ chmod a+x db_create.py
$ ./db_create.py
$ ./db_migrate.py
```

the output from the script should be:
```
New migration saved as db_repository/versions/001_migration.py
Current database version: 1
```

### Add admin user
Start a Python shell session

```
$ python
>>> from app import db
>>> from app.auth import models
>>> u =  models.User('[your username]','[your email]')
>>> u.password = [your password]
>>> u.password_hash
>>> u.role = 1   # 1 = admin
>>> u.status = 1 # 1 = active
>>> db.session.add(u)
>>> db.session.commit()
>>> print db.session.query(models.User.id).count() 
```

### Stop virtualenvironment
```
$ deactivate
```

## v0.2 silky sifaka
* Introduced template inheritance
* added flask-sqlalchemy and sqlalchemy-migrate for database connectivity
* added flask-wtf for web forms
* added functionality to sign up and login with username (email) and password
* added Bootstrap 
* introduced endangered primates for versioning :-)
