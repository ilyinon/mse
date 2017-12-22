import datetime

from django.db import models
from django.utils import timezone


class Version(models.Model):
    DEPRECATED = 0
    DEVELOPMENT = 1
    TESTING = 2
    ACTUAL = 3

    STATUS_VERSION = (
        (DEPRECATED, 'deprecated version'),
        (DEVELOPMENT, 'under development'),
        (TESTING, 'under testing'),
        (ACTUAL, 'producation ready'),
    )

    name = models.CharField(max_length=20)
    status = models.PositiveSmallIntegerField(choices=STATUS_VERSION, default='1', db_index=True)
    created = models.DateTimeField('date created', default=timezone.now(), db_index=True)

    def __str__(self):
        return self.name


class Region(models.Model):

    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created', db_index=True)

    def __str__(self):
        return self.name


class Server(models.Model):

    status_STOP = 0
    status_OPERATE = 1
    status_FAIL = 2
    status_DEPLOYING = 3
    status_MAINTAIN = 4
    status_NEW = 5

    STATUS_SERVER = (
        (status_STOP, 'stopped'),
        (status_OPERATE, 'operate'),
        (status_FAIL, 'failed'),
        (status_DEPLOYING, 'under deploying'),
        (status_MAINTAIN, 'under maintaining'),
        (status_NEW, 'just created'),
    )

    action_STOP = 0
    action_START = 1
    action_DEPLOY = 2
    action_MAINTAIN = 3
    action_DELETE = 4

    ACTION_SERVER =(
        (action_START, 'start server'),
        (action_STOP, 'stop server'),
        (action_DEPLOY, 'deploy server'),
        (action_MAINTAIN, 'send to maintain'),
        (action_DELETE, 'delete server'),
    )

    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField('date published', default=timezone.now(), db_index=True)
    updated = models.DateTimeField('date published', default=timezone.now())
    status = models.PositiveSmallIntegerField(choices=STATUS_SERVER, default=5, db_index=True)
    info = models.CharField(max_length=500)
    action = models.PositiveSmallIntegerField(choices=ACTION_SERVER, db_index=True, null=True)

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

    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('date created', default=timezone.now(), db_index=True)
    updated = models.DateTimeField('date updated', default=timezone.now())
    hosted_on = models.ForeignKey(Server, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_CLIENT, default=5, db_index=True)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def was_added_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)


