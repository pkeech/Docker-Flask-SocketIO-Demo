## IMPORT FLASK & EXTENSIONS
from flask import session
from flask_socketio import send, emit

## IMPORT SOCKETIO
from . import socketio

## DEFINE MESSAGE FUNCTION
@socketio.on('message')
def handleMessage(msg):
    print(f"Message Received: { msg }")
    send(msg, broadcast=True, namespace='/')

## DEFINE MESSAGE (API) FUNCTION
@socketio.on('messageAPI')
def handleMessageAPI(msg):
    print(f"Message Received (API): { msg }")
    send(msg, broadcast=True, namespace='/')