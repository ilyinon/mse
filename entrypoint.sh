#!/usr/bin/env sh

host=db
port=5432

echo -n "waiting for TCP connection to $host:$port..."

while ! nc -w 1 $host $port 2>/dev/null
do
  echo -n .
  sleep 1
done

echo 'ok'
sleep 5
/mse/mse/manage.py migrate --noinput
/mse/mse/manage.py collectstatic --noinput
uwsgi --ini /mse/uwsgi.ini
