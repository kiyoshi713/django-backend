from django.urls import path
from . import views

urlpatterns = [
    path("loginUsuario", views.loginUsuario)
]