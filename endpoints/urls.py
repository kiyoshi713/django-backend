from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("Carta", views.Carta),
    path("Categorias",views.CategoriasxRestaurante),
    path("Restaurantes", views.Restaurante),

    path("cuestionario", views.Formulario),

    path("loginRest", views.loginRestaurante),

    
]