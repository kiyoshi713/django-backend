from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente)
]