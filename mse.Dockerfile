FROM python:3.5-alpine

ARG WDIR="mse"
MAINTAINER devops
WORKDIR '/${WDIR}/'

ADD . /${WDIR}/
COPY ${WDIR}/docker_settings.py ${WDIR}/local_settings.py

RUN apk add --update postgresql-dev gcc musl-dev git\
    libevent-dev libffi-dev openssl-dev build-base yaml musl-dev linux-headers build-base python3-dev jpeg-dev zlib-dev\
    && pip3 install -r ./requirements.txt && pip3 install uwsgi

CMD '/${WDIR}/entrypoint.sh'
