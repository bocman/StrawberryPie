
from __future__ import absolute_import
"""
Django settings for project project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import djcelery
djcelery.setup_loader()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-v0nscxua4k3&mrr)gy#1_y(*&_-(5h33u-l&d-(-ut2^&@ro_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # Allow domain and subdomains]

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djcelery',
    'kombu.transport.django',
    'rest_framework',
    'webservice',
    'widget_tweaks',
    'djangosecure',
    'debug_toolbar',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'setting',
    'dashboard',
    'entertainment',
    'djangosecure'

)

DJANGO_SETTINGS_MODULE = "project.settings"

TEMPLATE_DIRS = (
    "%s/templates" % BASE_DIR,
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'djangosecure.middleware.SecurityMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS =( 
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
 
ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

#SECURE_SSL_REDIRECT = True

LOGIN_URL = "/"
LOGIN_REDIRECT_URL = "/dashboard/"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {}

import dj_database_url


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d5rqm4oh7gvrpc",
        "USER": "upbsznbuvgxsoz",
        "PASSWORD": "H6sNFivM6lAcnCFJ0cXwGUknWt",
        "HOST": "ec2-54-217-202-109.eu-west-1.compute.amazonaws.com",
        "PORT": "5432",
    }
}

# TODO permissions IsAdminUser
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('sl', _('Slovenian')),
    ('en', _('English')),
)

# "UTC", "Europe/Ljubljana"
TIME_ZONE = 'Europe/Ljubljana'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    '%s/static/' % BASE_DIR,
    '%s/static/images' % BASE_DIR,
)


#Enable it in production
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

FIXTURE_DIRS = (
    set(os.path.join(BASE_DIR, 'project/fixtures/'))
)

WEATHER_LOCATION = "Izola"
WEATHER_API_KEY = "1e408decf36cd52f"
WEATHER_API_LINK = "http://api.wunderground.com/api/"+ WEATHER_API_KEY+"/conditions/q/CA/"+WEATHER_LOCATION +".json"

# temperature unit, which is used at convertion
# Options: - KELVIN
#          - CELSIUS
#          - FAHRENHEIT
TEMPERATURE_UNIT = "CELSIUS"

# IP address of server
IP_ADDRESS = "192.168.1.130"

# Domain name of server
DOMAIN_NAME = "malina.webhop.me:8000"
 
#EMAIL SETTINGS
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'app41680308@heroku.com'
EMAIL_HOST_PASSWORD = 'ccqvqvpk7991'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

REDIS_URL = "ec2-54-195-242-227.eu-west-1.compute.amazonaws.com"
BROKER_URL = 'redis://h:pcaq1skmhhbgou5qk6t63iqik96@ec2-54-195-242-227.eu-west-1.compute.amazonaws.com:7739'
CELERY_RESULT_BACKEND= BROKER_URL
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_APP="proj"
CELERYD_NODES="worker"
CELERY_TIMEZONE = TIME_ZONE
 
