from django.forms import widgets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
from rest_framework.renderers import JSONRenderer
from serializers import ClientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings.models import Client

log = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET', 'POST'])
def clients(request, format=None):
    """
    List all code clients, or create a new client.
    """
    log.info("sem v logih")
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def client_detail(request, pk, format=None,):
    """
    Retrieve, update or delete a client instance.
    """
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ClientSerializer(pk=pk)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)