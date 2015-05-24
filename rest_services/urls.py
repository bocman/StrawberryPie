from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.client_detail),
)

urlpatterns = format_suffix_patterns(urlpatterns)