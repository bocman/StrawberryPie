from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    

    url(r'^logout/$', views.user_logout, name='user_logout'), 
    url(r'^general_settings/$', views.general_settings, name='general_settings'),

    url(r'^users/$', views.users_list, name='users_list'),
    url(r'^users/add/$', views.add_edit_user, name='add_user'),
    url(r'^users/edit/(?P<user_id>[0-9]+)/$', views.add_edit_user, name='edit_user'),
 
    url(r'^clients/$', views.clients_list, name='clients_list'), 
    url(r'^clients/$', views.clients_list, name='clients_list'),
    url(r'^clients/add/$', views.add_edit_client, name='add_client'),
    url(r'^clients/edit/(?P<client_id>[0-9]+)/$', views.add_edit_client, name='edit_client'),
    url(r'^clients/delete/(?P<client_id>[0-9]+)/$', views.delete_client, name='delete_client'),
    url(r'^clients/statistics/(?P<client_id>[0-9]+)/$', views.client_statistics, name='client_statistics'),
    
    url(r'^clients/notification_settings/(?P<client_id>[0-9]+)/$', views.edit_client_notification, name='edit_client_notification'),
)