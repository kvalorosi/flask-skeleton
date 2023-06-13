from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/')
def home():
    return {
        'Welcome home': 'There is no place like here'
    }

@app.route('/')
def test():
    return {
        'Is the mic on?': 'Is this function working??'
    }
