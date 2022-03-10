from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.settings import APP_SETTINGS
from src.utils.urls import build_urls


def create_app():
    app = Flask(__name__)
    app.config.from_object(APP_SETTINGS)
    from src.models import tables
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    build_urls(app)

    return app


application = create_app()
