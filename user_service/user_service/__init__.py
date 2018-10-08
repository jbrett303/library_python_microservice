# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/user.db'
db = SQLAlchemy(app)

from user_service import views
