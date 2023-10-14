from flask import Flask
from routes import main

from events import socketio

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret'

    app.register_blueprint(main)

    socketio.init_app(app)

    return app

app = create_app()

if __name__ == '__main__':
    socketio.run(app)