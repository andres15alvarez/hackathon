from rest_framework import serializers


class HomeSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True)
