from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.settings import HOST, PORT, APP_SETTINGS
from src.utils.urls import build_urls


def create_app():
    app = Flask(__name__)

    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True

    from src.models import tables
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    build_urls(app)

    return app


application = create_app()
