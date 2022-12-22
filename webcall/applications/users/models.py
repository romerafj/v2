

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager, moduloManager, agrupacionManager


class rol(models.Model):
    nombre = models.CharField(max_length=12, unique=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ["id"]

    def __str__(self):
        return str(self.id) + '-' + str(self.nombre)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    rol = models.ForeignKey(rol, on_delete=models.CASCADE, verbose_name="rol")
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombre + ' ' + self.apellidos


class modulo(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    destino = models.CharField(max_length=50)
    agrupacion = models.CharField(max_length=15, null=True)

    class Meta:
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
        ordering = ["id"]

    objects = moduloManager()

    def __str__(self):
        return str(self.id) + '-' + str(self.nombre)


class agrupacion (models.Model):

    rol = models.ForeignKey(rol, on_delete=models.CASCADE, verbose_name="rol")
    Modulo = models.ForeignKey(modulo, on_delete=models.CASCADE,
                               related_name='modulo_agrupacion', verbose_name="modulo")
    agrupacion = models.CharField(max_length=2, verbose_name="agrupacion")

    class Meta:
        verbose_name = "Agrupacion"
        verbose_name_plural = "Agrupaciones"
        ordering = ["id"]

    objects = agrupacionManager()

    def __str__(self):
        return str(self.rol) + '-' + str(self.Modulo) + '-' + str(self.agrupacion)
