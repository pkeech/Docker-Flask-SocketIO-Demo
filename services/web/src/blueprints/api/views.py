## IMPORT FLASK 
from flask import json, render_template, Blueprint, request, make_response, jsonify, redirect, url_for

## IMPORT EVENTS
from src.events import handleMessageAPI

## DEFINE BLUEPRINT
api = Blueprint('api', __name__, url_prefix='/api/v1')

## ENDPOINT: SEND MESSAGE
@api.route("/test", methods=['GET'])
def testRoute():
    ## TEST ADD MESSAGE
    if request.args.get("msg"):
        handleMessageAPI(f"[BOT] { request.args.get('msg') }")

        return jsonify({'message': 'Complete!'})

    ## ERROR HANDLE
    return jsonify({'message': 'ERROR!'})