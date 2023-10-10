from extensions import socketio

@socketio.on('connect')
def connect():
    print('Connected')