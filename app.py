from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sender")
def sender():
    return render_template("sender.html")

@app.route("/receiver")
def receiver():
    return render_template("receiver.html")

@socketio.on('message')
def handle_message(message):
    emit('response', {'data': message}, broadcast=True)