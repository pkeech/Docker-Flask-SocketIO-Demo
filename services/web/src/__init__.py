## IMPORT FLASK & EXTENSIONS
from flask import Flask
from .extensions import socketio

## IMPORT BLUEPRINTS
from .blueprints.pages.views import page
from .blueprints.api.views import api

## IMPORT SOCKETIO FUNCTIONS
import src.events

## [FOR DOCKER PURPOSES] Redirect Logs to STDOUT
import logging, os
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

## Define Flask Application
def create_app(settings_override=None):
    ## Create Application with Instance Folder
    app = Flask(__name__, instance_relative_config=True)

    ## Load Configurations
    app.config.from_object('src.config.settings')

    ## Initialize Extensions    
    extensions(app)

    ## Create Application Context
    with app.app_context():
        ## Register Blueprints
        app.register_blueprint(page)
        app.register_blueprint(api)

        ## Handle Logging
        app.logger.addHandler(stream_handler)

        ## Return Application
        return app

## Load (Stage) Flask Extensions
def extensions(app):
    ## Initialize Extensions
    socketio.init_app(app)