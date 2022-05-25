from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required

from .models import Pelicula, Review
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

    # Todas las reviews de la pelicula presentadas por fecha
    # en orden reverso.
    reviews = pelicula.review_set.order_by('-fecha')

    # Este bloque calcula la calificacion otorgada por
    # todas las reviews.
    calificacion = 0
    for review in reviews:
        calificacion += review.calificacion
    
    # Calcula la calificacion promedio
    calificacion = calificacion / len(reviews)
    # Redondear el numero a 2 decimales
    calificacion = round(calificacion, 2)

    context = {'pelicula': pelicula, 'reviews': reviews, 'calificacion': calificacion}
    return render(request, 'appIMDb/pelicula.html', context)

@login_required
def nuevaReview(request, pelicula_id):
    """ Aniade una nueva review a una pelicula. """

    pelicula = Pelicula.objects.get(id=pelicula_id)

    # Este bloque es un placeholder en lo que se implementa una view para
    # editar reviews.
    # Cuando el usuario tenga una review previa de una pelicula y quiera
    # realizar una segunda review, se le redireccionara a la pagina de
    # edicion de review, para que no pueda subir multiples reviews a una 
    # sola pelicula.
    """
    # Hace un query por todas las reviews de la pelicula
    reviews = pelicula.review_set.all()

    # Este bloque verificara si el usuario ha subido una review para esta pelicula
    # antes y en lugar de permitirle subir una nueva, le mostrara la misma.

    reviewPrevia = Review.objects.none() # Inicializa la variable con un queryset vacio
    for review in reviews:
        if review.usuario == request.user:
            reviewPrevia = review
    """

    if request.method != 'POST':
        # No se ha subido la informacion; crea un formulario en blanco.
        form = ReviewForm(initial={'pelicula': pelicula})
    else:
        # Datos POST subidos; procesar informacion.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            nuevaReview = form.save(commit=False)
            nuevaReview.pelicula = pelicula
            nuevaReview.usuario = request.user
            nuevaReview.save()
            return redirect('appIMDb:pelicula', pelicula_id=pelicula_id)

    # Muestra un formulario en blanco o invalido.
    context = {'pelicula': pelicula, 'form': form}
    return render(request, 'appIMDb/nuevaReview.html', context)

@login_required
def editarReview(request, review_id):
    """Edita una review existente"""

    review = Review.objects.get(id=review_id)

    pelicula = review.pelicula

    if request.method != 'POST':
        # Request inicial, pre-llena el formulario con la review actual.
        form = ReviewForm(instance=review)
    else:
        # Datos POST subidos; procesa los datos.
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('appIMDb:pelicula', pelicula_id=pelicula.id)

    context = {'review': review, 'pelicula': pelicula, 'form': form}
    return render(request, 'appIMDb/editarReview.html', context)