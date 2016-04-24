from django.forms import widgets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from setting.models import Client
from serializers import ClientSerializer

import logging

log = logging.getLogger(__name__)


class ClientsViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
























