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

def Cuestionario(request):
    if request.method != "POST":
        dictError={
            "error": "tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    dictCuestionario = json.loads(request.body)
    restaurante = dictCuestionario["restaurante"]
    valoracion = dictCuestionario["valoracion"]
    opinion = dictCuestionario["opinion"]

    cto = Form(restaurante=restaurante, valoracion=valoracion,opinion=opinion)
    cto.save()
    dictOk = {
        "error":""
    }
    return HttpResponse(json.dumps(dictOk))

@csrf_exempt        

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
                "cod":12345,
                "producto" : "Pizza Americana",
                "cliente": "Miley Cyrus",
                "estado": "Enviado"
            },
            {
                "id": 2,
                "cod":12346,
                "producto" : "Pizza Suprema",
                "cliente": "Alan Garcia",
                "estado": "Enviado"
            },
            {
                "id": 3,
                "cod":12349,
                "producto" : "Pizza Hawaiana",
                "cliente": "Renzo Cavero",
                "estado": "Enviado"
            }
        ]

        dictResponse = {
            "error":"",
            "pedido": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

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
    
def Actualizar_Pedido(request):
   
    if request.method != "POST":
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
    dictCategoria = json.loads(request.body)

    #Obtiene el objeto que pasó por body
    identificador = dictCategoria["id"]
    cat = Categoria.objects.get(pk=identificador) # Obtenemos cat de bd

    if dictCategoria.get("nombre") != None:
        cat.nombre = dictCategoria.get("nombre")

    if dictCategoria.get("estado") != None:
        cat.estado = dictCategoria.get("estado")

    cat.save() # Se modifica la bd

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))


def Verificar_EstadoPedido(request):
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
                "cod":12345,
                "producto" : "Pizza Americana",
                "cliente": "Miley Cyrus",
                "hora": "1 pm"
            },
            {
                "id": 2,
                "cod":12346,
                "producto" : "Pizza Suprema",
                "cliente": "Alan Garcia",
                "hora": "2 pm"
            },
            {
                "id": 3,
                "cod":12349,
                "producto" : "Pizza Hawaiana",
                "cliente": "Renzo Cavero",
                "hora": "3 pm"
            }]
        

        dictResponse = {
            "error":"",
            "pedido": lista
        }
        strResponse = json.dumps(dictResponse["pedido"])
        return HttpResponse(strResponse)

def obtenerListarestaurant(request):
    if request.method != "GET":
        dictError = {
            "error": "Tipo de peticion no existe."
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    else: 
        lista = [
            
                {
      id: 1,
      title: 'Papa Jhons',
      category: 'Pizzas',
      price: 1,
      img: "https://th.bing.com/th/id/R.0ca329b4241438c4d06b3f39bd16e962?rik=bXgCS839DVCFfw&riu=http%3a%2f%2flogos-download.com%2fwp-content%2fuploads%2f2016%2f04%2fPapa_Johns_logo_logotype.png&ehk=p7b60Mm79QFBKAYlCKbYN%2fYf2KZi6lBvEv8sedMa2TA%3d&risl=&pid=ImgRaw&r=0",
      desc: "Moderno",
    },
    {
      id: 2,
      title: 'Marcos Bistro',
      category: 'Pizzas',
      price: 2,
      img: "https://th.bing.com/th/id/R.8368c1fe7d4b0f652abd08ea0ff6a389?rik=YSTupaMFdJ4Tqg&pid=ImgRaw&r=0",
      desc: "Buen ambiente",
    },
    {
      id: 3,
      title: 'Pizza hat',
      category: 'Pizzas',
      price: 3,
      img: "https://th.bing.com/th/id/R.e2d6b11d6ebc867ca360f4ba29b24da8?rik=8JG7baUKZL49oA&riu=http%3a%2f%2fgraffica.info%2fwp-content%2fuploads%2f2017%2f07%2f2014-y-2016-EEUU-y-Asia.png&ehk=if8lDjJtIPdeMplfIqvSrxOQNhoViqYvxRkYLCwK2SU%3d&risl=&pid=ImgRaw&r=0",
      desc: "Atencion rapida",
    },
    {
      id: 4,
      title: 'Pardos chicken',
      category: 'Pollos',
      price: 1,
      img: "https://www.deliverylima.net/wp-content/uploads/2020/07/Pardos-Chicken-Logo.jpg",
      desc: "Lugar confortable",
    },
    {
      id: 5,
      title: 'Rockys',
      category: 'Pollos',
      price: 2,
      img: "https://th.bing.com/th/id/R.73a3a33c9467a036d052bf8f9a063318?rik=bYA8mrTpU0n3Qw&pid=ImgRaw&r=0",
      desc: "Para pasarlo en familia",
    },
  
    {
      id: 6,
      title: 'Mi barrunto',
      category: 'Mariscos',
      price: 1,
      img: "https://th.bing.com/th/id/R.9eb0c1eb981eee890f671f8d22574f7b?rik=lTlch1yo27JRPw&riu=http%3a%2f%2fwww.programasperu.com%2frestaurantes-peruanos%2fwp-content%2fuploads%2f2013%2f02%2fmi-barrunto.jpg&ehk=LLIUdlhR0tJuq1EIOj7d%2feT4CB2GlbX9qakNmLrow7A%3d&risl=&pid=ImgRaw&r=0",
      desc: "Ambinete confortable ",
    },
  
    {
      id: 7,
      title: 'Norkys',
      category: 'Pollos',
      price: 4,
      img: "https://th.bing.com/th/id/R.bae24ac4c043a603ec1d8585abbe0807?rik=W7kb6zdjHxkiGw&riu=http%3a%2f%2fnorkys.pe%2fwp-content%2fuploads%2f2020%2f09%2flogo.png&ehk=CTfH7OobnSj9nVkesF76XAG%2bSA8s%2fH%2bRiXj7wXYeLVY%3d&risl=&pid=ImgRaw&r=0",
      desc: "Ravioles rellenos de queso con salsa al pesto",
    },
  
    {
      id: 8,
      title: 'Puro tumbes',
      category: 'Mariscos',
      price: 1,
      img: "https://th.bing.com/th/id/R.01b46f534b501567bb108561f8991751?rik=vTPxJChgu748cg&riu=http%3a%2f%2f4.bp.blogspot.com%2f-6tGcuNHnMpM%2fUqDvfkhk5VI%2fAAAAAAAAAFQ%2fx-gKy8MFIc0%2fs1600%2flogo%2b1.jpg&ehk=7phLr0RQfkMFpuxyI87oNL3FsrN10iwhHdsvb1zAMVQ%3d&risl=&pid=ImgRaw&r=0",
      desc: "Productos frescos",
    },
  
    {
      id: 9,
      title: 'Punto azul',
      category: 'Mariscos',
      price: 2,
      img: "https://th.bing.com/th/id/OIP.Pn2kAYZcfO8s-LZi1ZEpxQHaHa?pid=ImgDet&rs=1",
      desc: "Hechos al instante",
    }
        ]

        dictResponse = {
            "error":"",
            "Categorias": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)        

