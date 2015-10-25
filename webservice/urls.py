from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
    url(r'^clients/$', views.clients, name='clients'),
)

urlpatterns = format_suffix_patterns(urlpatterns)