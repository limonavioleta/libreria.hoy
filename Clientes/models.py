from django.db import models

class InscripcionTaller(models.Model):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    taller = models.CharField(max_length=100, verbose_name="Nombre del Taller")
    alimento_donado = models.CharField(max_length=100, verbose_name="Alimento No Perecedero Donado")
    cupon = models.CharField(max_length=20, unique=True, blank=True, null=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.taller} (Cupón: {self.cupon})"