from django.urls import path


from . import views

urlpatterns = [
    path('', views.index_main, name='index_main'),
    path('server/', views.server_index, name='server_index'),
    path('client/', views.client_index, name='client_index'),
    path('version/', views.version_index, name='version_index'),
    path('server/<int:server_id>', views.server_client, name='server_client'),
    path('server/<int:server_id>/detail', views.server_detail, name='server_detail'),
    path('client/<int:client_id>/', views.client, name='detail'),
    path('client/add', views.add_new_client, name='add_new_client'),
    path('server/add', views.add_new_server, name='add_new_server'),
    path('version/add', views.add_new_version, name='add_new_version'),

]