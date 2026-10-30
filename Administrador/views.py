
from .models import Usuarios, Productos, Ventas_detalles
from .forms import UsuarioForm, ProductoForm, VentaDetalleForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def solo_administradores(view_func):
    """Decorador para asegurar que solo los administradores accedan a estas vistas."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_staff:
            messages.error(request, "No sos administrador, ingresa tu usuario.")
            return redirect('Clientes:index')
        return view_func(request, *args, **kwargs)
    return wrapper

# ==========================================
# 1. VISTAS DE LECTURA (READ)
# ==========================================

def index(request):
    return render(request, 'administrador/index.html')

def productos(request):
    lista_productos = Productos.objects.all()
    return render(request, 'administrador/productos.html', {'productos': lista_productos})

def usuarios(request):
    lista_usuarios = Usuarios.objects.all()
    return render(request, 'administrador/usuarios.html', {'usuarios': lista_usuarios})

def ventas_detalles(request):
    lista_ventas = Ventas_detalles.objects.all()
    return render(request, 'administrador/ventas_detalles.html', {'ventas': lista_ventas})

# Definimos 'ventas' como un alias de 'ventas_detalles' para que urls.py no falle
def ventas(request):
    return ventas_detalles(request)

# Alias adicionales por seguridad
def listar_productos(request): return productos(request)
def listar_usuarios(request): return usuarios(request)
def listar_ventas(request): return ventas_detalles(request)


# ==========================================
# 2. VISTAS DE CREACIÓN (CREATE)
# ==========================================

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'administrador/crear_producto.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'administrador/crear_usuario.html', {'form': form}) 

def crear_venta(request):
    if request.method == 'POST':
        form = VentaDetalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaDetalleForm()

    return render(request, 'administrador/crear_venta.html', {'form': form})


# ==========================================
# 3. VISTA DE BÚSQUEDA (Objetivo del PDF)
# ==========================================

def buscar_producto(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        resultados = Productos.objects.filter(nombre_producto__icontains=query)

    return render(request, 'administrador/buscar_producto.html', {
        'resultados': resultados,
        'query': query
    })


# ==========================================
# 4. VISTAS FALTANTES (Para evitar errores de URLs)
# ==========================================

def editar_producto(request, pk=None):
    pass

def eliminar_producto(request, pk=None):
    pass

def editar_usuario(request, pk=None):
    pass

def eliminar_usuario(request, pk=None):
    pass

def editar_venta(request, pk=None):
    pass

def eliminar_venta(request, pk=None):
    pass