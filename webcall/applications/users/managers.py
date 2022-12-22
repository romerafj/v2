
from django.db import models

from django.db.models import Count
#
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, rol, password, is_staff, is_superuser,  **extra_fields):
        user = self.model(
            username=username,
            rol=rol,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields

        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, rol, password=None, **extra_fields):
        return self._create_user(username, rol, password, False, False, **extra_fields)

    def create_superuser(self, username, rol, password=None, **extra_fields):
        return self._create_user(username, rol, password,  True, True,  **extra_fields)


class moduloManager(models.Manager):
    """ Manager para el modelo modulo"""

    def buscar_modulo(self, kword):
        # filtrar por un contenido de texto

        resultado = self.filter(
            destino__icontains=kword
        )
        return resultado

    def modulo_por_rol(self, rol):
        """Buscar un modulo por el rol"""

        return self.filter(
            modulo_agrupacion__rol__id=rol

        ).distinct()

    def modulo_por_rol_con_agrupacion(self):
        """Buscar un modulo por el rol añadiendo la agrupacion"""
        resultado = self.annotate(
            num_agrupacion=Count('modulo_agrupacion')
        ).order_by('agrupacion')

        for r in resultado:
            print('***********')
            print(r, r.num_agrupacion)

        return resultado


class agrupacionManager(models.Manager):
    """Managers para el modelo agrupacion"""

    def listar_agrupacion_por_rol(self, rol):
        """Sacar todas las agrupaciones de un rol"""
        return self.filter(
            rol__id=rol
        ).order_by('agrupacion')
