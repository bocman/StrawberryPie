# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from configurations import Configuration, values
from .celery import crontab

BASE_DIR = dirname(dirname(__file__))


class Common(Configuration):

    #APP CONFIGURATION
	INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_extensions'
    )

    THIRD_PARTY_APPS = (
        'djcelery',
        'kombu.transport.django',
        'rest_framework',
        'widget_tweaks',
        'djangosecure'
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'api',
        'setting',
        'dashboard',
        'entertainment'
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '-v0nscxua4k3&mrr)gy#1_y(*&_-(5h33u-l&d-(-ut2^&@ro_'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = ['*'] # Allow domain and subdomains]

    TEMPLATE_DEBUG = values.BooleanValue(True)

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

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'project',
            'USER': 'root',
            'PASSWORD': 'bostjanNovak1',
            'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
            'PORT': '3306',
            'OPTIONS': {
                "init_command": "SET foreign_key_checks = 0;",
            },
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

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

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
    DOMAIN_NAME = "malina.webhop.me"

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'bocman.novak@gmail.com'
    EMAIL_HOST_PASSWORD = 'bocmanadmin'
    EMAIL_PORT = 587

    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'filters': {
    #         'require_debug_false': {
    #             '()': 'django.utils.log.RequireDebugFalse'
    #         },
    #         'require_debug_true': {
    #             '()': 'django.utils.log.RequireDebugTrue'
    #         }
    #     },
    #     'formatters': {
    #         'main_formatter': {
    #             'format': '%(levelname)s:%(name)s: %(message)s '
    #             '(%(asctime)s; %(filename)s:%(lineno)d)',
    #             'datefmt': "%Y-%m-%d %H:%M:%S",
    #         },
    #     },
    #     'handlers': {
    #         'mail_admins': {
    #             'level': 'ERROR',
    #             'filters': ['require_debug_false'],
    #             'class': 'django.utils.log.AdminEmailHandler'
    #         },
    #         'console': {
    #             'level': 'DEBUG',
    #             'filters': ['require_debug_true'],
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'main_formatter',
    #         },
    #         'production_file': {
    #             'level': 'DEBUG',
    #             'class': 'logging.handlers.RotatingFileHandler',
    #             'filename': '/var/log/StrawberryPie/strawberry_info.log',
    #             'maxBytes': 1024 * 1024 * 5,  # 5 MB
    #             'backupCount': 7,
    #             'formatter': 'main_formatter',
    #             'filters': ['require_debug_false'],
    #         },
    #         'debug_file': {
    #             'level': 'DEBUG',
    #             'class': 'logging.handlers.RotatingFileHandler',
    #             'filename': '/var/log/StrawberryPie/strawberry.log',
    #             'maxBytes': 1024 * 1024 * 5,  # 5 MB
    #             'backupCount': 7,
    #             'formatter': 'main_formatter',
    #             'filters': ['require_debug_true'],
    #         },
    #         'null': {
    #             "class": 'django.utils.log.NullHandler',
    #         }
    #     },
    #     'loggers': {
    #         'django.request': {
    #             'handlers': ['mail_admins', 'console'],
    #             'level': 'ERROR',
    #             'propagate': True,
    #         },
    #         'django': {
    #             'handlers': ['null', ],
    #         },
    #         'py.warnings': {
    #             'handlers': ['null', ],
    #         },
    #         'django.db.backends': {
    #             'handlers': ['null'],  # Quiet by default!
    #             'propagate': False,
    #             'level':'DEBUG',
    #             },
    #         '': {
    #             'handlers': ['console', 'production_file', 'debug_file'],
    #             'level': "DEBUG",
    #         }
    #     }
    # }


    BROKER_URL = 'django://'
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend' 
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
    CELERY_APP="proj"
    CELERYD_NODES="worker"
    CELERY_TIMEZONE = TIME_ZONE