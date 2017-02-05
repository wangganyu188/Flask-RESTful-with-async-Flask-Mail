## Flask-Mail threaded example
-------

This project shows an example of a flask app that can send emails asynchronously.  It also demonstrates automated testing using pytest fixtures along with mocking thread calls.

Setting up a gmail account for this requires enabling IMAP in your gmail settings and then adding your username and password to the app.settings file in the DevConfig.  You may need to setup and use an [App password](https://support.google.com/mail/answer/185833) from gmail.

Add your settings to this configuration class or set them in your envinronment variables:
```python
class DevConfig(BaseConfig):
    """ A collection of settings to use during dev work """
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_DEBUG = True
```

##### Setting up your virtual environment
I create a directory in my home folder for holding all of my
python virtual environments
```bash
mkdir ~/python_virtual_envs
virtualenv ~/python_virtual_env/flask_mail_example_venv
source ~/python_virtual_env/flask_mail_example_venv/bin/activate
```

##### Installing the requirements
```bash
pip install -r reequirements.txt
```

##### Running the application
You can start the application via the ```run.py``` module:
```bash
python run.py
```
You can use GET parameters to customize the recipients and subject line:
```
http://127.0.0.1:5000/0.1/send_email/?recipients=[%27target_address@email.com%27]&subject=a%20simple%20email%20test

```

##### Running Automated Tests
Tests can be ran in your IDE or via the command line:
```bash
python -m pytest tests
```
