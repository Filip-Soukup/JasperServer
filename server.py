import socketio


class JServer:
    def __init__(self):
        self.socket = socketio.Server(cors_allowed_origins="*")
        self.users = []

        @self.socket.connect
        def connect(sid, environ):
            user_data = {'sid': sid, 'session': {}}
            user_session_data = self.session_data.get(sid, {})
            print(f"Client connected: {sid}")

    # Define an event handler for the 'message' event
    @self.socket.message
    def message(self, sid, data):
        print(f"Message from {sid}: {data}")
        sio.emit('message', data)

    # Define an event handler for the 'disconnect' event
    @self.socket.disconnect
    def disconnect(sid):
        print(f"Client disconnected: {sid}")

# Create a Socket.IO app and attach the server
app = socketio.WSGIApp(sio)