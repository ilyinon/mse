FROM python:3.5-alpine

RUN apk add --update postgresql-dev gcc git \
    libevent-dev libffi-dev openssl-dev yaml linux-headers musl-dev build-base python3-dev jpeg-dev zlib-dev
ADD ./ /code
COPY ./mse/docker_settings.py /code/mse/mse/settings.py
RUN pip install -r /code/requirements.txt
WORKDIR /code/mse
CMD ["celery", "-A", "mse", "worker","-l","debug","-f","celery.logs"]
