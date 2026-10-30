from django.urls import path
from . import views

urlpatterns = [
    # Rutas Productos
    path('productos/', views.productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    
    # LA RUTA NUEVA PARA EL BUSCADOR:
    path('productos/buscar/', views.buscar_producto, name='buscar_producto'),
    
    # Rutas Usuarios
    path('usuarios/', views.usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
# Rutas Ventas
    path('ventas/', views.ventas, name='listar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
]