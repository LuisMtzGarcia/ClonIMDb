"""Define los patrones URL para la app, appIMDb."""

from django.urls import path

from . import views

app_name = 'appIMDb'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pagina que muestra todas las peliculas.
    path('peliculas/', views.peliculas, name='peliculas'),
    # Pagina detallada para una pelicula individual.
    path('peliculas/<int:pelicula_id>/', views.pelicula, name='pelicula'),
    # Pagina que muestra todos los generos.
    path('generos/', views.generos, name='generos'),
    # Pagina que muestra todas las peliculas de un genero.
    path('generos/<int:genero_id>/', views.genero, name='genero'),
    # Pagina para escribir una review.
    path('review/<int:pelicula_id>/', views.nuevaReview, name='nuevaReview'),
    # Pagina para editar una review.
    path('review/editar/<int:review_id>/', views.editarReview, name='editarReview'),
]