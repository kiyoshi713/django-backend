from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
import json
from django.http import JsonResponse
from .models import Usuario
# /endpoints/login
@csrf_exempt
def loginUsuario(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        username = dictDataRequest["username"]
        password = dictDataRequest["password"]

        client = Usuario.objects.filter(username=username, password=password).first()

        if client:
            dictOk = {
                "error": "",
                "cliente":{
                    "username": client.username,
                    "password": client.password
                }
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            dictError = {
                "error": "No existe cuenta"
            }
            strError = json.dumps(username)
            return HttpResponse(strError)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
