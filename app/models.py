from datetime import datetime
from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow())

    def __repr__(self):
        return f'<Test {self.id}>'