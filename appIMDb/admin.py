from django.contrib import admin

from .models import Genero, Pelicula, Review

admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Review)