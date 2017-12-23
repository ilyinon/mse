FROM python:3.5-alpine

MAINTAINER devops
WORKDIR /mse/

ADD . /mse/
COPY /mse/docker_settings.py /mse/mse/mse/settings.py

RUN apk add --update  postgresql-dev gcc git \
    libevent-dev libffi-dev openssl-dev yaml linux-headers musl-dev build-base python3-dev jpeg-dev zlib-dev\
    && pip3 install -r /mse/requirements.txt && pip3 install uwsgi

CMD sh /mse/entrypoint.sh
