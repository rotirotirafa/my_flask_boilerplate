from flask_migrate import Migrate, MigrateCommand

migrate = Migrate()


def do_migration(app):
    migrate.init_app(app, app.db)
