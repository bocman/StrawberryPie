from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AdminPasswordChangeForm

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
  url(r'^entertainment/', include('entertainment.urls', namespace="entertainment")),
  url(r'^$', auth_views.login, {'template_name': 'project/index.html'}, name="login"),
  url(r'password/reset/$', auth_views.password_reset, 
        {'post_reset_redirect' : '/password/reset/done/',
        'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
  url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done' ),
  url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, 
        {'post_reset_redirect' : '/password/reset/complete/'}, name='password_reset_confirm'),
  url(r'^password/reset/complete/$', auth_views.password_reset_complete),
  )
