from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():  # put application's code here
    username = "Kirill"
    return render_template('index.html', username = username)
