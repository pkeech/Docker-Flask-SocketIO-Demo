## IMPORT FLASK 
from flask import render_template, Blueprint, request, make_response, jsonify, redirect, url_for

## IMPORT MODULES
import json, os, redis
from rq import Queue, Connection

## IMPORT TASKS
from src.tasks import background_task

## DEFINE BLUEPRINT
page = Blueprint('page', __name__, template_folder='templates')

## ROUTE: INDEX
@page.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

## ROUTE: TASKS DEMO
@page.route("/task", methods=['GET'])
def add_task():
    ## GET SUBMITTED STRING
    if request.args.get("n"):
        ## 
        with Connection(redis.from_url(os.getenv('REDIS_URL', 'redis://:Pa55w0rd@redis:6379/0'))):
            ## CREATE JOB
            q = Queue()
            job = q.enqueue(background_task, request.args.get("n"))

            ## CALCULATE NUMBER OF JOBS IN QUEUE
            q_len = len(q)

            ## RETURN CONFIRMATION
            return f"Task { job.id } added to the Queue at { job.enqueued_at }. { q_len } tasks in the queue"
            

    ## ERROR HANDLE
    return "No Value Received :("

## ROUTE SOCKET EXAMPLE (CHAT)
@page.route('/socket', methods=['GET'])
def socket():
    return render_template('socket.html')