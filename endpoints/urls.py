from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("Carta", views.Carta),
    path("Categorias",views.CategoriasxRestaurante),
    path("Restaurantes", views.Restaurante),
    path("cuestionario", views.Formulario),
    path("loginRest", views.loginRestaurante),
    path("Mostrar_ListaPedido", views.Mostrar_ListaPedido),
    path("registrarPedido",views.Registrar_EntregaPedido),
    path("actualizarPedido",views.Actualizar_Pedido),
    path("verificarPedido",views.Verificar_EstadoPedido)
]