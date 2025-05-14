from flask import Flask
from merlot.config.database import db, migrate
from merlot.routes import bp as main_bp
import os

def create_app():
    merlot = Flask(__name__)

    # Configuração
    merlot.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    merlot.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Extensões
    db.init_app(merlot)
    migrate.init_app(merlot, db)

    # Blueprints
    merlot.register_blueprint(main_bp)

    return merlot
