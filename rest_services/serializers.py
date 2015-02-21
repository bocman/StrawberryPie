from rest_framework import serializers

from settings.models import Client

class ClientSerializer(serializers.Serializer):


    class Meta:
        model = Client
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=15)
    description = serializers.CharField(max_length=30)
    ip_address = serializers.CharField(required=True)
    port = serializers.IntegerField(required=False)
    deleted = serializers.BooleanField()
    disabled = serializers.BooleanField()
    status = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance