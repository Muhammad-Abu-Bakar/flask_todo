from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

