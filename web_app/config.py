import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'a-csrf-secret-key'
    BCRYPT_LOG_ROUNDS = 12
    LOGIN_DISABLED = False
    LOGIN_MANAGER_SESSION_PROTECTION = 'strong'
    LOGIN_MANAGER_LOGIN_VIEW = 'login'
    LOGIN_MANAGER_REMEMBER_COOKIE_DURATION = 86400
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}