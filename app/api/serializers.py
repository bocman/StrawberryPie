from rest_framework import serializers

class ClientSerializer(serializers.Serializer):
    """
    Class is used to serialize data to Client object
    """
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=15)
    description = serializers.CharField(max_length=30)
    ip_address = serializers.CharField(required=True)
    port = serializers.IntegerField(required=False)
    deleted = serializers.BooleanField()
    disabled = serializers.BooleanField()
    key = serializers.CharField(max_length=80)

class ModulSerializer(serializers.Serializer):
    """
    Class is used to serialize data to Modul object
    """
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=30)
    is_general = serializers.BooleanField()
    pin_number = serializers.IntegerField()
    is_activated = serializers.BooleanField()


class GroupSerializer(serializers.Serializer):
    """
    Group serializer
    """
    name = serializers.CharField(max_length=40)
    description = serializers.CharField(max_length=50)
    is_deleted = serializers.BooleanField()