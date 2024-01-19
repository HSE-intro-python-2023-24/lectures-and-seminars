from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vasya'}
    posts = [
        {'author': {'username': 'Katya'},
         'body': 'Чудесная погодка!'},
        {'author': {'username': 'Kolya'},
         'body': 'На работе..:('}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)