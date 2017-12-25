from celery import shared_task
import os
import time
from .models import Server



@shared_task
def task_stop_server(server_id):
    server = Server.objects.get(id=server_id)
    server.action = 5
    server.status = 0
    server.save()
    return server.status


@shared_task
def task_start_server(server_id):
    server = Server.objects.get(id=server_id)
    server.action = 5
    server.status = 1
    server.save()
    return server.status


@shared_task
def task_deploy_server(server_id):
    server = Server.objects.get(id=server_id)
    server.action = 5
    server.status = 3
    server.save()
    return server.status


@shared_task
def task_maintain_server(server_id):
    server = Server.objects.get(id=server_id)
    server.action = 5
    server.status = 4
    server.save()
    return server.status


@shared_task
def task_delete_server(server_id):
    server = Server.objects.get(id=server_id)
    server.delete()
    return 1