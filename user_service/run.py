from user_service import create_app

app = create_app('dev.cfg')

#used to run local with python
if __name__ == "__main__":
    app.run()