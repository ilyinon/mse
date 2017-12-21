from django.contrib import admin
from .models import Server, Client, Version

admin.site.register(Server)
admin.site.register(Client)
admin.site.register(Version)
