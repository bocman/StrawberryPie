"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import djcelery

djcelery.setup_loader()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "/var/www/StrawberryPie/")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "/var/www/StrawberryPie/project/")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
