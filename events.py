from flask_socketio import emit
from flask import request
from extensions import socketio

users = {}

@socketio.on('connect')
def connect():
    pass

@socketio.on('user')
def user(username):
    users[request.sid] = username

@socketio.on('message')
def message(message):
    username = users[request.sid]
    emit('chat', {'message': message, "username": username}, broadcast=True)