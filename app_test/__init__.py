"""
On importe app dans __init__.py depuis views.py qui est ensuite importée dans main.py
"""
from app_test.views import app
from app_test import models

"""
Connect sqlalchemy to app
"""
models.db.init_app(app)
