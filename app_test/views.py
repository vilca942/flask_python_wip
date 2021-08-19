from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')  # le décorateur définit la route
@app.route('/index/')  # on peut définir plusieurs routes pour la même vue
def index():
    return render_template('index.html')  # pour afficher le template index.html sur cette route


@app.route('/result/')
def result():
    user_name = request.args.get('user_name')  # pour récupérer un paramètre passé dans /result/?user_name=xx
    return render_template('result.html', variable_name=user_name, booleen=True)  # on passe les variables au template


"""
int: ou autre pour caster la variable
Le paramètre est directement passé en variable de la fonction suite à l'appel de
l'url /result_bis/blabla
"""
@app.route('/result_bis/<string:variable_name>/')
def result_bis(variable_name):
    print(variable_name)
    return variable_name


"""
Make sure you created a 'config.py' file.
To get one variable --> app.config['MY_VARIABLE']
Ligne pour définir les configs de l'app à partir du fichier config.py situé à la racine du projet
"""
app.config.from_object('config')
