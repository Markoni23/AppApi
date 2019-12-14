from rest_framework import serializers, fields
from ..models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'info', 'api_token']
        read_only_fields = ('api_token',)