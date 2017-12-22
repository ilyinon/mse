from django.forms import ModelForm
from .models import Client, Server, Version


class ClientListForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'hosted_on', 'version')


class ServerListForm(ModelForm):
    class Meta:
        model = Server
        fields = ('name',)


class VersionListForm(ModelForm):
    class Meta:
        model = Version
        fields = ('name',)


class ServerChangeStatus(ModelForm):
    class Meta:
        model = Server
        fields = ('status',)
