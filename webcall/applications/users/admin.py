from django.contrib import admin

from .models import agrupacion, modulo, User, rol


admin.site.register(modulo)
admin.site.register(User)
admin.site.register(rol)
admin.site.register(agrupacion)
