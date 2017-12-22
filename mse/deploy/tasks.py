from celery import shared_task
import os
import time
from .models import Server


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def deploy_server(server_id):
    time.sleep(1)
    server = Server.objects.get(id=server_id)
    server.action = 5
    server.status = 3
    server.save()

    return server.status

