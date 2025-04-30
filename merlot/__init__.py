# merlot/__init__.py
from flask import Flask
from merlot.routes import bp  # importa seu blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)  # registra as rotas
    return app
