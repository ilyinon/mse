from django.forms import ModelForm
from .models import Client, Server


class ClientListForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'hosted_on')


class ServerListForm(ModelForm):
    class Meta:
        model = Server
        fields = ('name',)

