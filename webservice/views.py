from django.forms import widgets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from setting.models import Client
from serializers import ClientSerializer

import logging

log = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def clients(request, format=None):
    """
    List all code clients, or create a new client.
    """
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)
