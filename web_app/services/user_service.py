from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from web_app.models.User import User
from web_app import db, bcrypt

def register_user(form):
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()

def check_user(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        return True
    else:
        return False

def logout():
    logout_user()

@login_required
def get_current_user():
    return current_user

def check_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return True
    else:
        return False

def check_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False