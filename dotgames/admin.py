from django.contrib import admin

from . models import Genero, Juego, Autor

admin.site.register(Juego)
admin.site.register(Genero)
admin.site.register(Autor)

