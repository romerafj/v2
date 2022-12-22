from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class resultados (models.Model):

    resultado = models.CharField(max_length=15, verbose_name="Resultado")

    def __str__(self):
        return str(self.id) + '-' + str(self.resultado)

    class Meta:
        verbose_name = "Resultados"
        verbose_name_plural = "Resultados"
        ordering = ["id"]


class lead (models.Model):

    telefono = models.CharField(max_length=13, verbose_name="Teléfono")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    poblacion = models.CharField(max_length=50, verbose_name="Población")
    observaciones = models.TextField(
        verbose_name="Observaciones", null=True, blank=True)
    resultado = models.ForeignKey(resultados, on_delete=models. SET_NULL,
                                  verbose_name="resultado", null=True, default='Abierto')

    def __str__(self):
        return str(self.id) + '-' + str(self.nombre) + '-' + str(self.telefono)
