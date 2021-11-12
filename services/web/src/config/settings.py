## IMPORT PYTHON MODULES
import os

## FLASK SETTINGS
SECRET_KEY = 'MySuperSecretSecretKey'
APP_NAME = os.environ.get('APP_NAME', default="DemoApp")