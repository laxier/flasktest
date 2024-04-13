from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + "tasks.db"

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

from app import views