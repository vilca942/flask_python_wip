from flask_sqlalchemy import SQLAlchemy
from app_test.views import app

"""
Create database connection object
"""
db = SQLAlchemy(app)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.Integer(), nullable=True)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


db.create_all()
