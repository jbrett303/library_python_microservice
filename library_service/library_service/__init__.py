# third-party imports
from flask import Flask

app = Flask(__name__)

import library_service.views

from library_service.database import init_db
init_db()

from library_service.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()