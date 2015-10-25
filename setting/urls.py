from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    

    url(r'^logout/$', views.user_logout, name='user_logout'), 
    url(r'^general_settings/$', views.general_settings, name='general_settings'),

    url(r'^users/$', views.users_list, name='users_list'),
    url(r'^users/add/$', views.add_edit_user, name='add_user'),
    url(r'^users/edit/(?P<user_id>[0-9]+)/$', views.add_edit_user, name='edit_user'),

    url(r'^groups/$', views.groups_list, name='groups_list'),
    url(r'^groups/add/$', views.AddGroupView.as_view(), name='add_group'), 

    url(r'^moduls/$', views.ModulList.as_view(), name='moduls_list'),
    url(r'^moduls/add/$', views.ModulCreateView.as_view(), name='add_modul'),
    url(r'^moduls/delete/(?P<modul_id>[0-9]+)/$', views.delete_modul, name='delete_modul'),

    url(r'^clients/$', views.clients_list, name='clients_list'), 
    url(r'^clients/add/$', views.add_edit_client, name='add_client'),
    url(r'^clients/edit/(?P<client_id>[0-9]+)/$', views.add_edit_client, name='edit_client'),
    url(r'^clients/delete/(?P<client_id>[0-9]+)/$', views.ClientDeleteView.as_view(), name='delete_client'),
    url(r'^clients/statistics/(?P<client_id>[0-9]+)/$', views.client_statistics, name='client_statistics'),   
    url(r'^clients/notification_settings/(?P<client_id>[0-9]+)/$', views.edit_client_notification, name='edit_client_notification'),
    url(r'^clients/shutdown/(?P<client_id>[0-9]+)/$', views.shutdown_client, name='shutdown_client'),

    url(r'^moduls/activate/(?P<client_id>[0-9]+)/(?P<pin_number>[0-9]+)/(?P<status>[A-Za-z]+)/$', views.activate_modul, name='activate_modul'), 

    url(r'^events/add/$', views.AddEventView.as_view(), name='add_event'),
    url(r'^events/edit/(?P<pk>[0-9]+)/$', views.EditEventView.as_view(), name='edit_event'),
)