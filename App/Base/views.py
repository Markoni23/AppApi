from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import App
from .utils import random_api
from os import sys
# Create your views here.

def change_token(request, pk):
    app = App.objects.get(pk= pk)
    app.api_token = random_api()
    data = { "new_token": app.api_token}
    print(data, file = sys.stderr)
    print(app.api_token, file = sys.stderr)
    app.save()
    return JsonResponse(data)

def info_by_token(request, token):
    app = App.objects.get(api_token=token)
    data = model_to_dict(app)
    return JsonResponse(data)