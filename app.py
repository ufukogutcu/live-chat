from flask import Flask
from routes import main

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'

app.register_blueprint(main)