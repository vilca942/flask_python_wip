"""
To generate a new secret key:
>>> import random, string
>>> "".join([random.choice(string.printable) for _ in range(24)])
La secret key est obligatoire
"""
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_APP_ID = 1200420960103822  # à supprimer si inutile
