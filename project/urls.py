from django.conf.urls import patterns, include, url
from django.contrib import admin

import logging


log = logging.getLogger(__name__)



urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
  url(r'^settings/', include('settings.urls', namespace='settings')),
  url(r'^webservice/', include('rest_services.urls', namespace="webservice")),
  
  url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'project/index.html', 'redirect_field_name': 'nekaj.html'}),

  )
