from django.forms import widgets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from setting.models import Client
from serializers import ClientSerializer

import json
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


@api_view(['GET', 'PATCH'])
def client_detail(request, key, data=None,):
    log.info("Im in the client detail")
    log.info(request.method)
    """
    Get or update client information/s
    """
    try:
        log.info("sem pred pridobi podatke")
        client = Client.objects.get(key=key)
        log.info(" ----------------------" )
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        new_data = request.data
        try:
            log.info("i' get data, sucesss")
            Client.objects.filter(key=key).update(**new_data)
            log.debug("Client '%s' has been updated", (client.name))
            return Response(status=status.HTTP_200_OK)
        except:
            log.debug("Client '%s' failed to be updated", (client.name))
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)
