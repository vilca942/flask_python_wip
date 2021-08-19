"""
On importe app dans __init__.py depuis views.py qui est ensuite importée dans main.py
"""
from app_test.views import app
from app_test import models

"""
Connect sqlalchemy to app
"""
models.db.init_app(app)


"""
Le décorateur permet d'ajouter un paramètre init-db à la ligne de commande du client flask.
Ce qui permet de lancer l'initialisation de la bdd en ligne de commande :
FLASK_APP=main.py flask init-db
Attention! flask init-db et pas flask init_db (wtf)
"""
@app.cli.command()
def init_db():
    models.init_db()
