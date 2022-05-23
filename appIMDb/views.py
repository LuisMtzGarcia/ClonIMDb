from django.shortcuts import render

from .models import Pelicula

def index(request):
    """ La home page para la app. """
    return render(request, 'appIMDb/index.html')

def peliculas(request):
    """ Muestra todas las peliculas. """
    peliculas = Pelicula.objects.order_by('titulo')

    context = {'peliculas': peliculas}
    return render(request, 'appIMDb/peliculas.html', context)

def pelicula(request, pelicula_id):
    """ Muestra los detalles de una pelicula. """
    pelicula = Pelicula.objects.get(id=pelicula_id)

    context = {'pelicula': pelicula}
    return render(request, 'appIMDb/pelicula.html', context)