from flask import Flask
from src.database.connection import db
from src.database.migrate import migrate

from src import config
from src.settings import APP_SETTINGS
from src.utils.urls import build_urls


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Development)

    from src.models.tables import User
    db.init_app(app)
    migrate.init_app(app, db)

    build_urls(app)

    return app


application = create_app()
