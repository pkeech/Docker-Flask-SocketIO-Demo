## BASE IMAGE
FROM redis:6.2.6 AS builder
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"

## IMAGE DEPENDENCIES
FROM builder AS dependencies

## DEV IMAGE
FROM dependencies AS development
## TODO: MAKE REDIS PASSWORD ENVIRONMENT VARIABLE
CMD ["redis-server", "--requirepass Pa55w0rd"]

## TEST IMAGE
FROM dependencies AS test

## PRODUCTION IMAGE
FROM dependencies AS production
## TODO: MAKE REDIS PASSWORD ENVIRONMENT VARIABLE
CMD ["redis-server", "--requirepass Pa55w0rd"]