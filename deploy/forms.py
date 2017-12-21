from django.forms import ModelForm
from .models import Client


class ServerListForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'hosted_on')




