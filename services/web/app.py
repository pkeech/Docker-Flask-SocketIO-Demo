## IMPORT APPLICATION
from src import create_app, socketio

## CREATE APPLICATION
app = create_app()

## RUN APPLICATION
if __name__ == "__main__":
    socketio.run(app)