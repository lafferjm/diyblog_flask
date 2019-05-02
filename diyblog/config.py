import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User configuration
    USER_ENABLE_EMAIL = False

    USER_LOGIN_URL = '/accounts/login'
    USER_LOGIN_TEMPLATE = 'auth/login.html'

    USER_LOGOUT_URL = '/accounts/logout'
    
    USER_REGISTER_URL = '/accounts/register'
    USER_REGISTER_TEMPLATE = 'auth/register.html'

    USER_ENABLE_REMEMBER_ME = False
