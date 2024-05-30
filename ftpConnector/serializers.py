from rest_framework import serializers

class FTPRequestSerializer(serializers.Serializer):
    hostname = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200, write_only=True)
    pathname = serializers.CharField(max_length=500)