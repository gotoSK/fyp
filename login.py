# login.py
from flask import redirect, render_template, url_for, session, flash, request
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


def create_default_admin():
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        admin = User(username='admin', is_admin=True,
                     email='admin@example.com')
        admin.set_password('order_match')  # Set the password for the admin
        db.session.add(admin)
        db.session.commit()


def login(request):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            if user.is_admin:
                return redirect(url_for('routes.admin_dashboard'))
            else:
                return redirect(url_for('routes.user_dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')
