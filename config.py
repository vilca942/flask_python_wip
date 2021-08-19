import os

"""
Ce fichier config.py recense toutes les variables globales nécessaires
à la configuration de l'app.
"""

"""
To generate a new secret key:
>>> import random, string
>>> "".join([random.choice(string.printable) for _ in range(24)])
La secret key est obligatoire pour la configuration de l'app
"""
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_APP_ID = 1200420960103822  # à supprimer si inutile

"""
Cette ligne indique à l'ORM SQLAlchemy l'url de la bdd app.db : 
"""
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


SQLALCHEMY_TRACK_MODIFICATIONS = False  # ligne pour éviter un warning de SQLAlchemy
