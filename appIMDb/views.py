from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404

from .models import Pelicula, Review, Genero
from .forms import ReviewForm

def index(request):
    """ La home page para la app. """
    return render(request, 'appIMDb/index.html')

def peliculas(request):
    """ Muestra todas las peliculas. """
    peliculas = Pelicula.objects.order_by('-anio')

    context = {'peliculas': peliculas}
    return render(request, 'appIMDb/peliculas.html', context)

def pelicula(request, pelicula_id):
    """ Muestra los detalles de una pelicula. """
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    # Todas las reviews de la pelicula presentadas por fecha
    # en orden reverso.
    reviews = pelicula.review_set.order_by('-fecha')

    # Este bloque calcula la calificacion otorgada por
    # todas las reviews.
    calificacion = None
    for review in reviews:
        # Si no hay reviews, calificacion se mantiene como None.
        if calificacion == None:
            calificacion = 0
        calificacion += review.calificacion

    # Redondear el numero a 2 decimales
    if calificacion != None:
        # Calcula la calificacion promedio, evita la division de 0 si es el resultado
        # de las sumas. 
        # Si la suma total de calificacion es 0, no hay necesidad de obtener el
        # promedio; todos habrian votado 0.
        if calificacion > 0:
            calificacion = calificacion / len(reviews)
            calificacion = round(calificacion, 2) 

    # Verifica si el usuario la ha marcado como favorita o no
    if pelicula.favoritos.filter(id=request.user.id).exists():
        # Esta flag dira si el usuario la ha marcado como favorita antes.
        favFlag = True
    else:
        favFlag = False

    context = {'pelicula': pelicula, 'reviews': reviews, 'calificacion': calificacion,
                'favFlag': favFlag}
    return render(request, 'appIMDb/pelicula.html', context)

def peliculasRating(request):
    """Muestra todas las peliculas ordenadas por su Rating, 
        en orden de mayor a menor."""

    peliculas = Pelicula.objects.order_by('titulo')

    # Dict para almacenar las peliculas junto a sus calificaciones.
    calificaciones = {}

    for pelicula in peliculas:
        calificaciones[pelicula] = 0
        calificacion = 0
        reviews = pelicula.review_set.order_by('-fecha')
        for review in reviews:
            calificacion += review.calificacion
        if len(reviews) > 0:
            calificaciones[pelicula] = calificacion / len(reviews)
        else:
            calificaciones[pelicula] = 0

    # Organiza el dict de mayor a menor calificacion.
    sortedCalificaciones = dict(sorted(calificaciones.items(),
                                        key=lambda item: item[1],
                                        reverse=True))

    peliculasCalificaciones = sortedCalificaciones.keys()

    context = {'peliculas': peliculasCalificaciones}
    return render(request, 'appIMDb/peliculasRating.html', context)

def peliculasFavorito(request):
    """Muestra todas las peliculas, ordenadas por el numero de usuarios que las
        ha marcado como favoritos, de mayor a menor."""

    peliculas = Pelicula.objects.order_by('titulo')

    # Dict para almacenar las peliculas y su numero de favoritos.
    favoritosDict = {}

    # Calcula el numero de favoritos por pelicula.
    for pelicula in peliculas:
        favoritosDict[pelicula] = 0
        favoritos = pelicula.favoritos.all()
        for favorito in favoritos:
            favoritosDict[pelicula] += 1

    # Organiza el dict de mayor a menor.
    sortedFavoritos = dict(sorted(favoritosDict.items(),
                                    key=lambda item: item[1],
                                    reverse=True))

    context = {'peliculas': sortedFavoritos.keys()}
    return render(request, 'appIMDb/peliculasFavoritos.html', context)
        


def generos(request):
    """Muestra todos los generos de peliculas disponibles."""

    generos = Genero.objects.order_by('nombre')

    context = {'generos': generos}
    return render(request, 'appIMDb/generos.html', context)

def genero(request, genero_id):
    """Muestra todas las peliculas de un genero elegido."""

    genero = get_object_or_404(Genero, id=genero_id)

    peliculas = genero.pelicula_set.order_by('titulo')

    context = {'genero': genero, 'peliculas': peliculas}
    return render(request, 'appIMDb/genero.html', context)

@login_required
def nuevaReview(request, pelicula_id):
    """ Aniade una nueva review a una pelicula. """

    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    # Este bloque verificara si el usuario ha subido una review para esta pelicula
    # antes y en lugar de permitirle subir una nueva, lo redireccionara para
    # que edite esa review.
    # Esto se hace para que los usuarios solo puedan dejar un review por pelicula,
    # y asi, no manipular la calificacion de la pelicula.
    # Por muy buena que este Morbius, vivimos en una democracia.

    # Filtra las reviews de la pelicula, para checar si el usuario ha hecho una
    # review antes para esta pelicula.
    review = pelicula.review_set.filter(usuario=request.user)

    # Un queryset vacio es falsy, por lo que solo se ejecutaria si existe una
    # review previa. Se toma el id de esta y se redirecciona a editarla.
    if review:
        return redirect('appIMDb:editarReview', review_id=review[0].id)


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

    review = get_object_or_404(Review, id=review_id)

    # Verifica que la review por editar sea del usuario.
    if review.usuario != request.user:
        raise Http404

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

@login_required
def borrarReview(request, review_id):
    """Elimina una review existente."""
    review = get_object_or_404(Review, id=review_id)

    pelicula = get_object_or_404(Pelicula, id=review.pelicula.id)
    # Verifica que la review por borrar sea del usuario.
    if review.usuario.username == request.user.username:
        review.delete()
        return redirect('appIMDb:pelicula', pelicula_id=pelicula.id)
    else:
        raise PermissionDenied