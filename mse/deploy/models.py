import datetime

from django.db import models
from django.utils import timezone


class Version(models.Model):

    name = models.CharField(max_length=20)
    created = models.DateTimeField('date created', db_index=True)

    def __str__(self):
        return self.name


class Server(models.Model):

    STOP = 0
    OPERATE = 1
    FAIL = 2
    DEPLOYING = 3
    MAINTAIN = 4
    NEW = 5
    STATUS_SERVER = (
        (STOP, 'stopped'),
        (OPERATE, 'started'),
        (FAIL, 'failed'),
        (DEPLOYING, 'under deploying'),
        (MAINTAIN, 'under maintaining'),
        (NEW, 'just created'),
    )

    name = models.CharField(max_length=200)
    created = models.DateTimeField('date published', db_index=True)
    updated = models.DateTimeField('date published')
    status = models.PositiveSmallIntegerField(choices=STATUS_SERVER, db_index=True)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def was_added_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

    def server_list(self):
        return self.name


class Client(models.Model):

    STOP = 0
    OPERATE = 1
    UPDATING = 2
    MAINTAIN = 3
    FAIL = 4
    NEW = 5
    STATUS_CLIENT = (
        (STOP, 'stopped'),
        (OPERATE, 'started'),
        (UPDATING, 'under updating'),
        (MAINTAIN, 'under maintaining'),
        (FAIL, ' failed'),
        (NEW, 'just created'),
    )

    name = models.CharField(max_length=100)
    created = models.DateTimeField('date created', db_index=True)
    updated = models.DateTimeField('date updated')
    hosted_on = models.ForeignKey(Server, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_CLIENT, db_index=True)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def was_added_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)

