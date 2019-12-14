from ..models import App
from .serializers import AppSerializer
from rest_framework import viewsets
from os import sys


class AppViewset(viewsets.ModelViewSet):
     queryset = App.objects.all()
     serializer_class = AppSerializer