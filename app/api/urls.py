from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = patterns('',
   url(r'^clients/$', views.ClientsViewSet.as_view({'get': 'list'}), name='clients')
 #  url(r'^groups/$', views.GroupsViewSet.as_view({'get': 'list'}), name='groups')
)

urlpatterns = format_suffix_patterns(urlpatterns)