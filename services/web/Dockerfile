## DEFINE BASE IMAGE
## TODO: PYTHON CAN BE UPDATED ONCE EVENTLET WORKS WITH PYTHON > 3.9
## https://stackoverflow.com/questions/69473317/eventlet-throws-error-on-import-in-docker
FROM python:3.9.8-slim-buster AS builder

## ADD METADATA
LABEL Maintainer="Peter Keech <peter@dodbrit.com>"

## INCLUDE IMAGE REQUIREMENTS
RUN apt update && apt install -y curl gnupg2 gcc

##  ======================
##  ==== APPLICATION =====
##  ======================

## DEFINE APPLICATION IMAGE
FROM builder as application

## SET WORKING DIRECTORY
WORKDIR /src

## ADD ONLY REQUIREMENTS TO LEVEAGE DOCKER CACHE SYSTEM
COPY requirements.txt /src/requirements.txt

## INSTALL APPLICAION DEPENDENCIES
RUN pip install -r requirements.txt

## ADD APPLICATION SOURCE
COPY . /src

##  ======================
##  ====    TASKS    =====
##  ======================

## DEFINE TASKS IMAGE
FROM application as tasks

## DEFINE ENVIRONMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## START WORKER
## TODO: MAKE THE CONNECTION STRING AN ENVIRONMENT VARIABLE
CMD ["rq", "worker", "-u", "redis://:Pa55w0rd@redis:6379"]

##  ======================
##  ==== DEVELOPMENT =====
##  ======================

## DEFINE DEVELOPMENT IMAGE
FROM application as development

## DEFINE ENVIRONMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=development \
    FLASK_RUN_PORT=8080 \
    FLASK_APP=app.py

## DEFINE PORT
EXPOSE 8080

## START APPLICATION
CMD ["flask", "run", "--host=0.0.0.0"]

##  ======================
##  =====    TEST    =====
##  ======================

## DEFINE TEST IMAGE
FROM application AS test

## INSTALL TEST TOOLS
RUN pip install flake8

##  ======================
##  ===== PRODUCTION =====
##  ======================

## DEFINE PRODUCTION IMAGE
FROM application as production

## DEFINE ENVIRONMENT VARIABLES
ENV FLASK_ENV=production

## START APPLICATION WITH UWSGI
CMD ["uwsgi", "app.ini"]