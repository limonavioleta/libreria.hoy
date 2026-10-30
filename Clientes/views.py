from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def solo_clientes(view_func):
    """Decorador para asegurar que los administradores no entren a las vistas de clientes."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('clientes:login')
        if request.user.is_staff:
            messages.error(request, "No sos cliente, sos administrador.")
            return redirect('Administrador:index')
        return view_func(request, *args, **kwargs)
    return wrapper

def login_view(request):
    """Vista para manejar el inicio de sesión de los usuarios."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.is_staff:
                return redirect('Administrador:index')
            else:
                return redirect('clientes:index')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'clientes/login.html', {'form': form})

@solo_clientes
def index(request):
    return render(request, 'clientes/index.html')

@solo_clientes
def reservar_libro(request):
    return render(request, 'clientes/reservar_libro.html')

@solo_clientes
def crear_lector(request):
    return render(request, 'clientes/crear_lector.html')

@solo_clientes
def listar_lectores(request):
    return render(request, 'clientes/listar_lectores.html')

@solo_clientes
def inscribir_taller(request):
    return render(request, 'clientes/inscribir_taller.html')