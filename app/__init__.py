from flask import Flask
from config import Config
from views import nlu_bp, get_ready


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Call the get_ready() function from the views.py to get the NLP engine
    # ready.
    get_ready()
    app.register_blueprint(nlu_bp)
    return app
