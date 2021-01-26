from flask import Flask
from .views import page

app = Flask(__name__)


def create_app():
    app.register_blueprint(page)
    return app