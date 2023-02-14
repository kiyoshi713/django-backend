from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import Categoria, Platos

# /endpoints/login
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        if usuario == "alumno" and password == "123":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def obtenerPlatos(request):
    if request.method == "GET":
        idCat = request.GET.get("categoria")

        if idCat == None:
            dictError = {
                "error" : "Enviar categoria."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        platosFiltr = []

        if idCat == "-1":
            platosQS = Platos.objects.all()
        else:
            platosQS = Platos.objects.filter(categoria__pk=idCat)
        
        for i in platosQS:
            platosFiltr.append({
                "id": i.pk ,
                "title": i.nombre,
                "price": float(i.precio),
                "img": i.img,
                "desc": i.dscr,
                "category": i.categoria.nombre 
            })

        dictResponse = {
            "error": "",
            "carta": platosFiltr
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt   
def obtenerCategorias(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoria.objects.all()
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id":c.id,
                "nombre":c.nombre
            })
        dictOK = {
            "error" : " ",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

"""
ID Registro , Categoria , Fecha

"""
def obtenerRegistroCat(request):
    if request.method != "GET":
        dictError = {
            "error": "Tipo de peticion no existe."
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    else: 
        lista = [
            {
                "id": 1,
                "categoria": "Pizzas",
                "Fecha Registro" : "01-01-2023"
            },
            {
                "id": 2,
                "categoria": "Pastas",
                "Fecha Registro" : "01-01-2023"
            },
            {
                "id": 3,
                "categoria": "Bebidas",
                "Fecha Registro" : "01-01-2023"
            }
        ]

        dictResponse = {
            "error":"",
            "Categorias": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

