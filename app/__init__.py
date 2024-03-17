from flask import Flask

from blueprint import httpbin


def create_app():
    app = Flask(__name__)
    app.register_blueprint(httpbin)
    return app
