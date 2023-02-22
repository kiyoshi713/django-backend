from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("cuestionario", views.Formulario),
    path("restaurant/listar", views.obtenerListarestaurant), 
    path("restaurant/categorias", views.Mostrar_Catego)
]