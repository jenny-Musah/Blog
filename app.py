from flask import Flask
from application_bean import return_server
import controller.UserController

app = return_server()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
