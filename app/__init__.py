"""
    This package holds the files needed to configure and
    build the flask wsgi app.

       -  Settings for how the app is configured are located in
          the settings module

       -  Flaks extensions like Flask Mail are instantiated in
          the extensions module in an unconfigured state and then
          initialized in the app building process

       -  The app configuration/creation occurs in the flask_app
          module in the create_app function.

       -  Api routes are located in the api_endpoints package and
          then attached to the app via the register_endpoints
          method located in the endpoints module

       -  A demo of the WSGI app can be ran via the run.py file
          and opening a browser to localhost:5000/0.1/send_email/
          will send an email to the values set in your settings
          DevConfig class
"""
from .extensions import api
from .extensions import mail
from .flask_app import app
from .flask_app import create_app
