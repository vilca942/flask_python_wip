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
Cette ligne indique à l'ORM SQLAlchemy l'url de la bdd mysql : 
'mysql://username:password@localhost/db_name'
"""
SQLALCHEMY_DATABASE_URI = 'mysql://test_user:mysql@localhost/flask_test_bdd'
