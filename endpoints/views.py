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

        if usuario == "cliente" and password == "123":
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
                "fecha": "01-01-2023"
            },
            {
                "id": 2,
                "categoria": "Pastas",
                "fecha" : "01-01-2023"
            },
            {
                "id": 3,
                "categoria": "Bebidas",
                "fecha": "01-01-2023"
            }
        ]

        dictResponse = {
            "error":"",
            "Categorias": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

"""
ID Registro, Plato, Categoria, Descripcion, Fecha Registro

"""
def obtenerRegistroPlato(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")
        if categoria == None:
            dictError = {
                "error": "Enviar categoria."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        lista = [
            {
                "id": 1,
                "nombre": "Pizza Americana Familiar",
                "categoria": "Pizzas",
                "descripcion": "aeaeaeaeaa",
                "fecha" : "01-01-2023"
            },{
                "id": 2,
                "nombre": "Tallarines",
                "categoria": "Pastas",
                "descripcion": "aeaeaeaeaa",
                "fecha" : "01-01-2023"
            },{
                "id": 3,
                "nombre": "Inca Kola",
                "categoria": "Bebidas",
                "descripcion": "aeaeaeaeaa",
                "fecha" : "01-01-2023"
            }
        ]

        platosFiltr = []
        if categoria == "-1":
            platosFiltr=lista
        else:
            for i in lista:
                if i["categoria"] == int(categoria):
                    platosFiltr.append(i)
        
        dictResponse = {
            "error": "",
            "platos": list(platosFiltr)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe.0"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
        
def loginRestaurante(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        if usuario == "trabajador" and password == "valv123":
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

def Registrar_EntregaPedido(request):
    return 0

def Mostrar_ListaPedido(request):
    return 0

def Verificar_EstadoPedido(request):
    return 0