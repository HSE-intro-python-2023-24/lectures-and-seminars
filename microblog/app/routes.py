from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import app
from app import db
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {'author': {'username': 'Katya'},
         'body': 'Чудесная погодка!'},
        {'author': {'username': 'Kolya'},
         'body': 'На работе..:('}
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None:
            flash('Invalid username')
            rd = redirect(url_for('login'))
        if not user.check_password(form.password.data):
            flash('Invalid password')
            rd = redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        rd = redirect(url_for('index'))

        return rd
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    