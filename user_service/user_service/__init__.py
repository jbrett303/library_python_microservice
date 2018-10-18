"""app factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def create_app(config=None):
    """creates the app instance"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config)
    register_extension(app)
    register_blueprints(app)
    return app

def register_extension(app):
    """register extensions with the app, in this case just the db"""
    DB.init_app(app)

def register_blueprints(app):
    """register blueprints to the app"""
    from user_service.views import USER_ROUTES
    app.register_blueprint(USER_ROUTES)
