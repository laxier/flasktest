from app import app, db
from flask import render_template, request, redirect
from app.models import ToDo


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    if request.method == "POST":
        task = request.form['content']
        new_task = ToDo(content = task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was the error"
    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    to_delete = ToDo.query.get_or_404(id)

    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem"

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    task = ToDo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['updated']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem"
    else:
        return render_template('edit.html', task = task)
