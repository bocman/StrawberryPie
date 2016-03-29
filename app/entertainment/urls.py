from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
  url(r'^music/$', views.music.as_view(), name='music'),
    )
