# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config)
    register_extension(app)
    register_blueprints(app)
    return app

def register_extension(app):
    db.init_app(app)

def register_blueprints(app):
    from user_service.views import user_routes
    app.register_blueprint(user_routes)
