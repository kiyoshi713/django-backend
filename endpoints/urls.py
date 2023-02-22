from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("cuestionario", views.Formulario),
    path("loginRest", views.loginRestaurante),
]