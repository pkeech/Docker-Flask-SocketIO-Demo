## BASE IMAGE
FROM python:3.9.1-alpine AS builder
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"

## IMAGE DEPENDENCIES
FROM builder AS dependencies

## INSTALL REQUIREMENTS
RUN pip install rq-dashboard

## FIX CLICK INCOMPATIBILITY BUG
## https://github.com/Parallels/rq-dashboard/pull/385
## https://github.com/Parallels/rq-dashboard/issues/387
COPY ./cli.py /usr/local/lib/python3.9/site-packages/rq_dashboard/cli.py

## PRODUCTION IMAGE
FROM dependencies AS production

## EXPOSE REQUIRED PORTS
EXPOSE 9181

## START APPLICATION
## TODO: MAKE REDIS CONNECTION ENVIRONMENT VARIABLE
#ENTRYPOINT ["python3", "-m", "rq_dashboard", "--redis-url", "redis://:Pa55w0rd@redis:6379"]
CMD ["rq-dashboard", "--redis-url", "redis://:Pa55w0rd@redis:6379"]