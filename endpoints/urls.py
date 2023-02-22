from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("cuestionario", views.Formulario),
<<<<<<< HEAD
    path("loginRest", views.loginRestaurante),
=======
    path("restaurant/listar", views.obtenerListarestaurant), 
    path("restaurant/categorias", views.Mostrar_Catego)
>>>>>>> 38110f7bba922a6a3f45873ba74da7a9d77646c3
]