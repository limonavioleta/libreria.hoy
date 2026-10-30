from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('reservar/', views.reservar_libro, name='reservar_libro'),
    path('crear/', views.crear_lector, name='crear_lector'),
    path('listar/', views.listar_lectores, name='listar_lectores'),
    path('inscribir/', views.inscribir_taller, name='inscribir_taller'),
]