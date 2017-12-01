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
>>> u.role = models.Role.ADMIN
>>> u.status = models.Status.ACTIVE
>>> db.session.add(u)
>>> db.session.commit()
>>> models.User.query.all() 
>>> 
```

### Add gmail credentials to your environment
Assuming gmail is your test e-mail server
```
$ export MAIL_USERNAME=[gmail username]
$ export MAIL_PASSWORD=[gmail password]
```
Let's see whether it works:
```
$ python
>>> from config import MAIL_USERNAME
>>> from flask_mail import Message
>>> from app import app
>>> print MAIL_USERNAME
>>> msg = Message('test subject', sender='you@example.com', recipients=['[RECIPIENT EMAIL]'])
>>> msg.body='test body'
>>> with app.app_context():
>>> ...mail.send(msg)
>>> 
```

### Run the application!
```
$ python ./run.py
```

### Stop virtualenvironment
```
$ deactivate
```

## v0.2 silky sifaka
* added functionality to sign up and login with username (email) and password
* introduced template inheritance
* added flask-sqlalchemy and sqlalchemy-migrate for database connectivity
* added flask-wtf for web forms
* added flask-mail for e-mail confirmation
* added Bootstrap 
* introduced endangered primates for version naming
