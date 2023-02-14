from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("categorias/listar", views.obtenerCategorias),
    path("platos/listar", views.obtenerPlatos),
    path("hist/cat", views.obtenerRegistroCat),
    path("hist/plato", views.obtenerRegistroPlato),
    path("loginRestaurante", views.loginRestaurante)
]