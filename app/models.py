from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(100), nullable=False)


class Besticons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(10), nullable=False)
    iconurl = db.Column(db.String(100), nullable=False)
