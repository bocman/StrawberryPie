from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
    url(r'^ping/$', views.ping, name='ping'),

    url(r'^clients/$', views.clients, name='clients'),
    url(r'^clients/(?P<key>[0-9A-Za-z]+)/$', views.client_detail),
)

urlpatterns = format_suffix_patterns(urlpatterns)