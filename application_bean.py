from flask import Flask

app = Flask(__name__)


def return_server():
    return app
