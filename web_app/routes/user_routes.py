```python
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from web_app.models.User import User
from web_app.services.user_service import check_password_hash, generate_password_hash
from web_app import db, bcrypt

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully.', 'login_message')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username/password.', 'login_message')
    return render_template('login.html')

@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'logout_message')
    return redirect(url_for('login'))

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'register_message')
        return redirect(url_for('login'))
    return render_template('register.html')
```