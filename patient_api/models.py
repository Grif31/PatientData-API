from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Patient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    condition = db.Column(db.String(120))