from flask import Flask
from routes import main

from events import socketio

def run_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret'

    app.register_blueprint(main)

    socketio.init_app(app)

    socketio.run(app)