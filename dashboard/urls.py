from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
  url(r'^$', views.dashboard, name="dashboard"),
    )
