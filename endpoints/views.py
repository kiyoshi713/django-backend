from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import Cliente, Restaurant,Plato,Categoria_Plato,Form, CategoriasporRestaurante

# /endpoints/login
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        username = dictDataRequest["username"]
        password = dictDataRequest["password"]

        client = Cliente.objects.filter(username=username, password=password).first()

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

@csrf_exempt
def loginRestaurante(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        Rest = Restaurant.objects.filter(usuario=usuario, password=password).first()

        if Rest:
            # Correcto
            dictOk = {
                "error": "",
                "restaurante":{
                    "usuario": Rest.usuario,
                    "password": Rest.password
                }
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(usuario)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
def Mostrar_ListaPedido(request):
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
                "cod":12347,
                "producto" : "Pizza Americana",
                "precio": "32 soles",
                "estado": "Enviado"
            },
            {
                "id": 2,
                "cod":12346,
                "producto" : "Pizza Suprema",
                "precio": "42 soles",
                "estado": "Enviado"
            },
            {
                "id": 3,
                "cod":12349,
                "producto" : "Pizza Hawaiana",
                "precio": "35 soles",
                "estado": "Finalizado"
            },
            
        ]

        dictResponse = {
            "error":"",
            "pedido": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

def Restaurante(request):
    #http://127.0.0.1:8000/endpoints/Restaurantes?id=1
     if request.method=="GET":
         restaurante = request.GET.get("id")
         if restaurante == None:
             dictError = {
                 "error" : "Enviar restaurante."
             }
             strError = json.dumps(dictError)
             return HttpResponse(strError)
        
         restFiltr = []

         if restaurante == "-1":
             restQS = Restaurant.objects.all()
         else:
             restQS = Restaurant.objects.filter(id = restaurante)
         for i in restQS:
             restFiltr.append({
                 "id": i.id,
                 "nombre": i.nombre,
                 "desc": i.descripcion,
                 "img": i.logo
             })
         dictResponse = {
             "error": " ",
             "restaurantes": restFiltr
         }
         strResponse = json.dumps(dictResponse)
         return HttpResponse(strResponse)
     else:
         dictError={
             "error": "Tipo de peticion no existe"
         }
         strError = json.dumps(dictError)
         return HttpResponse(strError)

def Carta(request):
    #http://127.0.0.1:8000/endpoints/Carta?categoria=-1&restaurant=2
    
    if request.method == "GET":
        restaurant = request.GET.get("restaurant")
        categoria = request.GET.get("categoria")
        if restaurant==None and categoria==None:
            dictError = {
                "error": "Enviar restaurante y categoria como query parameter"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        CartaQuerySet = Plato.objects.all()
        listaCarta = []

        if categoria == "-1":
            CartaQuerySet = Plato.objects.filter(restaurante__pk=restaurant)
            for i in CartaQuerySet:
                listaCarta.append({
                    "id":i.id,
                    "title":i.nombre,
                    "price": float(i.precio),
                    "desc": i.dscr,
                    "img": i.img,
                    "restaurante":{
                        "idRest": i.restaurante.id,
                        "nombreRest": i.restaurante.nombre
                    },
                    "categoria":{
                        "idCat": i.categoria.id,
                        "nombreCat": i.categoria.nombre
                    }   
                })
        else:
            CartaQuerySet = Plato.objects.filter(restaurante__pk=restaurant, categoria__pk=categoria)
            for i in CartaQuerySet:
                listaCarta.append({
                    "id":i.id,
                    "title":i.nombre,
                    "price": float(i.precio),
                    "desc": i.dscr,
                    "img": i.img,
                    "restaurante":{
                        "idRest": i.restaurante.id,
                        "nombreRest": i.restaurante.nombre
                    },
                    "categoria":{
                        "idCat": i.categoria.id,
                        "nombreCat": i.categoria.nombre
                    }
                })
        dictResponse = {
            "error":" ",
            "carta": list(listaCarta)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError={
            "error": "Peticion no existe",
        }
        strError=json.dumps(dictError)
        return HttpResponse(strError)

def CategoriasxRestaurante(request):
    #http://127.0.0.1:8000/endpoints/Categorias?restaurant=-1
    if request.method=="GET":
        restaurant = request.GET.get("restaurant")

        if restaurant==None:
            dictError={
                "error": "Enviar categoria"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        CategoriasFiltradas = []

        if restaurant=="-1":
            categoriasQS = CategoriasporRestaurante.objects.filter
        else:
            categoriasQS = CategoriasporRestaurante.objects.filter(restaurant__pk=restaurant)
        for i in categoriasQS:
            CategoriasFiltradas.append({
                "id":i.categoria.id,
                "categoria": i.categoria.nombre
            })
        dictResponse = {
            "error": " ",
            "categorias": CategoriasFiltradas
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError={
            "error": "Peticion no existe"
        }
        strError=json.dumps(dictError)
        return HttpResponse(strError)
