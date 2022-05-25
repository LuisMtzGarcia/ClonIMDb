""" Define los patrones URL para users. """

from django.urls import path, include

from . import views

app_name = "urls"
urlpatterns = [
    # Incluye las urls de auth default.
    path('', include('django.contrib.auth.urls')),
    # Pagina para crear una cuenta.
    path('registro/', views.registro, name='registro'),
    # Pagina para visualizar las peliculas favoritas.
    path('perfil/favoritas', views.listaFav, name='listaFav'),
    # Pagina para agregar a favoritos.
    path('fav/<int:pelicula_id>/', views.marcarFav, name='marcarFav', ),
]