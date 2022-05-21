from django.contrib import admin

from .models import Pelicula, Review, Rating

admin.site.register(Pelicula)
admin.site.register(Review)
admin.site.register(Rating)