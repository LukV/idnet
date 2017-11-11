# idnet

idnet is a typical web application, based on the Python microframework Flask. idnet's aim is to put the GDPR to work. Users can upload their personal data from Google, Facebook etc to idnet which then vizualizes the data and how it is used.

## Installation

### Set up Python, pip and virtualenv
Make sure to have python 3.6 and install additional packages:
* python-dev (development tools)
* pip (to manage packages)
* virtualenv (to create isolated, virtual

$ mkdir idnet
$ cd idnet
$ virtualenv -p /usr/bin/python3.6 env

### Start virtualenvironment
$ source env/bin/activate

### Install packages
$ pip install flask
$ pip install flask-babel

### Freeze current state
$ pip freeze > requirements.txt

See the list of installed packages without the requirements format using “pip list”. Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

$ pip install -r requirements.txt

### Stop virtualenvironment
$ deactivate

## Features master branch

v 0.1
* uses flask Blueprint for modularity
* i8n with 2 languages 'en', 'nl' using flask-babel gettext implementation

