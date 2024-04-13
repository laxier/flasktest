from app import app
from flask import render_template, request
from app.models import ToDo


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    if request.method == "POST":
        task = request.form['content']
        new_task = ToDo(content = task)
    else:
        return render_template('index.html')
