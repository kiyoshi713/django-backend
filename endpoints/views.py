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


        def Mostrar_Catego(request):
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
                "nombres":"Pizzas",
            },
            {
                "id": 2,
                "nombres":"Mariscos",
            },
            {
                "id": 3,
                "nombres":"Pollos",
            },
            
        ]

        dictResponse = {
            "error":"",
            "categorias": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

def obtenerListarestaurant(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")

        if categoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        restaurant = [
            {
      "id": 1,
      "title": 'Papa Jhons',
      "categoria": 1,
      "price": 1,
      "img": "https://th.bing.com/th/id/R.0ca329b4241438c4d06b3f39bd16e962?rik=bXgCS839DVCFfw&riu=http%3a%2f%2flogos-download.com%2fwp-content%2fuploads%2f2016%2f04%2fPapa_Johns_logo_logotype.png&ehk=p7b60Mm79QFBKAYlCKbYN%2fYf2KZi6lBvEv8sedMa2TA%3d&risl=&pid=ImgRaw&r=0",
      "desc": "Moderno",
    },
    {
      "id": 2,
      "title": 'Marcos Bistro',
      "categoria": 1,
      "price": 2,
      "img": "https://th.bing.com/th/id/R.8368c1fe7d4b0f652abd08ea0ff6a389?rik=YSTupaMFdJ4Tqg&pid=ImgRaw&r=0",
      "desc": "Buen ambiente",
    },
    {
      "id": 3,
      "title": 'Pizza hat',
      "categoria": 1,
      "price": 3,
      "img": "https://th.bing.com/th/id/R.e2d6b11d6ebc867ca360f4ba29b24da8?rik=8JG7baUKZL49oA&riu=http%3a%2f%2fgraffica.info%2fwp-content%2fuploads%2f2017%2f07%2f2014-y-2016-EEUU-y-Asia.png&ehk=if8lDjJtIPdeMplfIqvSrxOQNhoViqYvxRkYLCwK2SU%3d&risl=&pid=ImgRaw&r=0",
      "desc": "Atencion rapida",
    },
    {
      "id": 4,
      "title": 'Pardos chicken',
      "categoria": 3,
      "price": 1,
      "img": "https://www.deliverylima.net/wp-content/uploads/2020/07/Pardos-Chicken-Logo.jpg",
      "desc": "Lugar confortable",
    },
    {
      "id": 5,
      "title": 'Rockys',
      "categoria": 3,
      "price": 2,
      "img": "https://th.bing.com/th/id/R.73a3a33c9467a036d052bf8f9a063318?rik=bYA8mrTpU0n3Qw&pid=ImgRaw&r=0",
      "desc": "Para pasarlo en familia",
    },
  
    {
      "id": 6,
      "title": 'Mi barrunto',
      "categoria": 2,
      "price": 1,
      "img": "https://th.bing.com/th/id/R.9eb0c1eb981eee890f671f8d22574f7b?rik=lTlch1yo27JRPw&riu=http%3a%2f%2fwww.programasperu.com%2frestaurantes-peruanos%2fwp-content%2fuploads%2f2013%2f02%2fmi-barrunto.jpg&ehk=LLIUdlhR0tJuq1EIOj7d%2feT4CB2GlbX9qakNmLrow7A%3d&risl=&pid=ImgRaw&r=0",
      "desc": "Ambinete confortable ",
    },
  
    {
      "id": 7,
      "title": 'Norkys',
      "categoria": 3,
      "price": 4,
      "img": "https://th.bing.com/th/id/R.bae24ac4c043a603ec1d8585abbe0807?rik=W7kb6zdjHxkiGw&riu=http%3a%2f%2fnorkys.pe%2fwp-content%2fuploads%2f2020%2f09%2flogo.png&ehk=CTfH7OobnSj9nVkesF76XAG%2bSA8s%2fH%2bRiXj7wXYeLVY%3d&risl=&pid=ImgRaw&r=0",
      "desc": "Ravioles rellenos de queso con salsa al pesto",
    },
  
    {
      "id": 8,
      "title": 'Puro tumbes',
      "categoria": 2,
      "price": 1,
      "img": "https://th.bing.com/th/id/R.01b46f534b501567bb108561f8991751?rik=vTPxJChgu748cg&riu=http%3a%2f%2f4.bp.blogspot.com%2f-6tGcuNHnMpM%2fUqDvfkhk5VI%2fAAAAAAAAAFQ%2fx-gKy8MFIc0%2fs1600%2flogo%2b1.jpg&ehk=7phLr0RQfkMFpuxyI87oNL3FsrN10iwhHdsvb1zAMVQ%3d&risl=&pid=ImgRaw&r=0",
      "desc": "Productos frescos",
    },
  
    {
      "id": 9,
      "title": 'Punto azul',
      "categoria": 2,
      "price": 2,
      "img": "https://th.bing.com/th/id/OIP.Pn2kAYZcfO8s-LZi1ZEpxQHaHa?pid=ImgDet&rs=1",
      "desc": "Hechos al instante",
    }
                
        ]

        restaurantFiltradas = []

        if categoria == "-1":
            # No se debe filtrar nana
            restaurantFiltradas = restaurant
        else :
            for p in restaurant:
                if p["categoria"] == int(categoria):
                    restaurantFiltradas.append(p)
        

        # TODO: Consultas a bd
        dictResponse = {
            "error": "",
            "restaurante": list(restaurantFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)