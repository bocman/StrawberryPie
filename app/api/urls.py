from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import viewsets

urlpatterns = patterns('',
   url(r'^$', viewsets.api_root),
   url(r'^clients/$', viewsets.ClientViewSet.as_view({'get': 'list'}), name='client-list'),
   url(r'^groups/$', viewsets.GroupViewSet.as_view({'get': 'list'}), name='group-list')
)

urlpatterns = format_suffix_patterns(urlpatterns)
