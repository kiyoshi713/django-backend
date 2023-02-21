from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import Cliente, Restaurant,Plato, Restaurant_Cat,Categoria_Plato,Form,Menu

# /endpoints/login
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        username = dictDataRequest["username"]
        password = dictDataRequest["password"]

        clientes = Cliente.objects.filter(username=username, password=password)

        if clientes:
            dictOk = {
                "error": "",
                "cliente":{
                    "username": clientes.username,
                    "password": clientes.password
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

def Formulario(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        cliente = dictDataRequest["cliente"]
        rest = dictDataRequest["rest"]
        comentario = dictDataRequest["comentario"]
        Valoracion_cuantificacion = dictDataRequest["Valoracion_cuantificacion"] 
        
        frm = Form(cliente=cliente, rest=rest, comentario=comentario,Valoracion_cuantificacion=Valoracion_cuantificacion)
        frm.save()
        dictOk = {
            "error": " "
        }
        return HttpResponse(json.dumps(dictOk))
    else:
        dictError = {
            "error" : "tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)