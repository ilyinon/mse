from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.db.models import Count
from . import forms
from django.utils import timezone

from .models import Server, Client, Version


def index_main(request):
    context = {client:server_detail}
    return render(request, 'deploy/index.html', context)


def server_index(request):
    server_list = Server.objects.annotate(num_client=Count('client')).order_by('created')
    form = forms.ServerListForm()
    context = {
        'form': form,
        'server_list': server_list, }
    return render(request, 'servers/index.html', context)


def server_client(request, server_id):
    client_list_on_server = Client.objects.filter(hosted_on=server_id)
    context = {'client_list_on_server': client_list_on_server, }
    return render(request, 'servers/client_list.html', context)


def client_index(request):
    client_list = Client.objects.order_by('id')
    paginator = Paginator(client_list, 5)
    form = forms.ClientListForm()
    page = request.GET.get('page')
    client_list = paginator.get_page(page)

    context = {
        'form': form,
        'client_list': client_list,
    }
    return render(request, 'clients/index.html', context)

def version_index(request):
    version_list = Version.objects.annotate().order_by('name')
    form = forms.VersionListForm()
    context ={
        'form': form,
        'version_list': version_list,
    }
    return render(request, 'version/index.html', context)

def server_detail(request, server_id):
    server_info = get_object_or_404(Server, pk=server_id)

    context = {
        'server_info': server_info,
    }
    return render(request, 'servers/detail.html', context)


def client(request, client_id):
    client_info = get_object_or_404(Client, pk=client_id)
    context = {
        'client_info': client_info,
    }
    return render(request, 'clients/client.html', context)


def add_new_client(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.ClientListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            f = form.save(commit=False)
            f.created = timezone.now()
            f.updated = timezone.now()

            f.status = 5

            f.save()
            return HttpResponseRedirect('/client')

    return HttpResponseRedirect()


def add_new_server(request):
    if request.method == 'POST':
        form = forms.ServerListForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.created = timezone.now()
            f.updated = timezone.now()
            f.info = "none"
            f.status = 5

            f.save()
            return HttpResponseRedirect('/server')

    return HttpResponseRedirect()


def add_new_version(request):
    if request.method == 'POST':
        form = forms.VersionListForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return HttpResponseRedirect('/version')
    return HttpResponseRedirect()