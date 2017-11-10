#IDNet

##Set up Python, pip and virtualenv
Make sure to have python 3.6 and install additional packages:
* python-dev (development tools)
* pip (to manage packages)
* virtualenv (to create isolated, virtual

##Installation
$ mkdir idnet
$ cd idnet
$ virtualenv -p /usr/bin/python3.6 env

###Start virtualenvironment
$ source env/bin/activate

###Install packages
$ pip install flask

###Freeze current state
$ pip freeze > requirements.txt

See the list of installed packages without the requirements format using “pip list”. Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

$ pip install -r requirements.txt

Lastly, Exclude from source control by adding it to the ignore list: the virtual environment folder, __pycache__

###Stop virtualenvironment
$ deactivate


