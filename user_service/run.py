"""run to create the app instance and run the server"""
from user_service import create_app

APP = create_app('dev.cfg')

#used to run local with python
if __name__ == "__main__":
    APP.run()
