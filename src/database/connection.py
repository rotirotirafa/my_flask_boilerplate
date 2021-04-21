from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_connection(app):
    db.init_app(app)
    app.db = db