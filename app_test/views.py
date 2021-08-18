from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"


"""
Ligne pour définir les configs de l'app à partir du fichier config.py situé à la racine du projet
Make sure you created a 'config.py' file.
To get one variable --> app.config['MY_VARIABLE']
"""
app.config.from_object('config')


