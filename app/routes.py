from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mikey boi'}
    posts = [
            {'author': {'username':'Mikey boi'}, 'body': 'Feeling fly'},
            {'author': {'username':'Lainers'}, 'body': 'Jumpin an hollerin'}
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
