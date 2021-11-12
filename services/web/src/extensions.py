## IMPORT REQUIRED PYTHON MODULES
import os 
 
## IMPORT EXTENSIONS
from flask_socketio import SocketIO


## INITIALIZE EXTENTIONS
## TODO: REPLACE STATIC VARIABLES WITH ENV VARIABLES
#celeryapp = Celery(broker=os.environ.get("CELERY_BROKER_URL", default="redis://:Pa55w0rd!@redis:6379/0"))
socketio = SocketIO()
