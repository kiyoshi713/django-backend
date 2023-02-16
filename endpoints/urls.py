from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente", views.loginCliente),
    path("categorias/listar", views.obtenerCategorias),
    path("platos/listar", views.obtenerPlatos),
    path("hist/cat", views.obtenerRegistroCat),
    path("hist/plato", views.obtenerRegistroPlato),
    path("loginRestaurante", views.loginRestaurante),
    path("pedidoRelizado", views.Mostrar_ListaPedido),
    path("registrarPedido",views.Registrar_EntregaPedido),
    path("actualizarPedido",views.Actualizar_Pedido),
    path("cuestionario", views.Cuestionario),
    path("verificarPedido",views.Verificar_EstadoPedido)
]