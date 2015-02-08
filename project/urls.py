from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings/', include('settings.urls', namespace='settings')),

        url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'project/index.html', 'redirect_field_name': 'nekaj.html'}),
    #url(r'^/lost_password$', 'django.contrib.auth.views.password_reset' name="lost_password")
)
