# third-party imports
from flask import Flask

app = Flask(__name__)

import user_service.views

from user_service.database import init_db
init_db()

from user_service.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()