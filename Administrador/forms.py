from django import forms
from .models import Usuarios, Productos, Ventas_detalles

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre_usuario', 'email_usuario']
        labels = {
            'nombre_usuario': 'Nombre del Usuario',
            'email_usuario': 'Correo Electrónico',
        }
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Perez'}),
            'email_usuario': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@email.com'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre_producto', 'marca_producto']
        labels = {
            'nombre_producto': 'Nombre del Producto',
            'marca_producto': 'Marca',
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Teclado'}),
            'marca_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Logitech'}),
        }


class VentaDetalleForm(forms.ModelForm):
    class Meta:
        model = Ventas_detalles
        fields = ['monto', 'fecha_venta', 'forma_de_pago', 'producto', 'usuario']
        labels = {
            'monto': 'Monto ($)',
            'fecha_venta': 'Fecha de Venta',
            'forma_de_pago': 'Forma de Pago',
            'producto': 'Producto',
            'usuario': 'Usuario / Cliente',
        }
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'forma_de_pago': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Efectivo, Tarjeta, etc.'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'usuario': forms.Select(attrs={'class': 'form-select'}),
        }