from rest_framework import serializers

from models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        
        fields = (
            'name', 'description', 'ip_address',
            'port', 'deleted', 'disabled', 'status'
        )

    def list(self, request):
        pass
