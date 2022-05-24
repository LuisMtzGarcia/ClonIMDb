from gzip import READ
from django.shortcuts import render,  redirect

from .models import Pelicula
from .forms import ReviewForm

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

def nuevaReview(request, pelicula_id):
    """ Aniade una nueva review a una pelicula. """

    pelicula = Pelicula.objects.get(id=pelicula_id)

    if request.method != 'POST':
        # No se ha subido la informacion; crea un formulario en blanco.
        form = ReviewForm(initial={'pelicula': pelicula})
    else:
        # Datos POST subidos; procesar informacion.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            nuevaReview = form.save(commit=False)
            nuevaReview.pelicula = pelicula
            nuevaReview.save()
            return redirect('appIMDb:pelicula', pelicula_id=pelicula_id)

    # Muestra un formulario en blanco o invalido.
    context = {'pelicula': pelicula, 'form': form}
    return render(request, 'appIMDb/nuevaReview.html', context)