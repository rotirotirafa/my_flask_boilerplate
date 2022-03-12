from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from src import config
from src.settings import APP_SETTINGS
from src.utils.urls import build_urls

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    teste = Column(String(1000))
    books = Column(String(1))
    table = Column(String(2))


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Development)

    db.init_app(app)
    migrate.init_app(app, db)

    build_urls(app)

    return app


application = create_app()
