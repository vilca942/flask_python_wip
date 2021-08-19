from flask_sqlalchemy import SQLAlchemy
from app_test.views import app
import logging  # pour la gestion des logs

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


class Gender:
    FEMALE = 0
    MALE = 1
    OTHER = 2


"""
La création des objets n'est plus faite via cette instruction mais 
dans la fonction init_db ci-dessous.
Celle-ci est appelée depuis __init__.py
"""
# db.create_all()


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content('description 1', Gender.MALE))
    db.session.add(Content('description 2', Gender.FEMALE))
    db.session.commit()
    logging.warning('Database initialized!')  # pour afficher un log
