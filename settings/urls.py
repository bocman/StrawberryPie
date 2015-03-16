from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    

    url(r'^logout/$', views.user_logout, name='user_logout'), 

    url(r'^clients/$', views.clients_list, name='clients_list'), 
    url(r'^clients/$', views.clients_list, name='clients_list'),
    url(r'^clients/add/$', views.add_edit_client, name='add_client'),
    url(r'^clients/edit/(?P<client_id>[0-9]+)/$', views.add_edit_client, name='edit_client'),
    url(r'^clients/delete/(?P<client_id>[0-9]+)/$', views.delete_client, name='delete_client'),
)