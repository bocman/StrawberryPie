from django.forms import widgets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from serializers import ClientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings.models import Client


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
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk, format=None,):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)