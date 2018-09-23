from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app import views

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    bootstrap.init_app(app)
    db.init_app(app)
    views.init_app(app)
    return app
