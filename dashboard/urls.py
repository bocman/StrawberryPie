from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
                       url(r'^dashboard/$', views.test_dashboard, name="test_dashboard"
                           ),
                       )
