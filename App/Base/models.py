from django.db import models
from .utils import random_api


class App(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=150)
    api_token =  models.CharField(max_length = 17,  default = random_api)

