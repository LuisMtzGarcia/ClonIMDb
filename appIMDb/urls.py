"""Define los patrones URL para la app, appIMDb."""

from django.urls import path

from . import views

app_name = 'appIMDb'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pagina que muestra todas las peliculas.
    path('peliculas/', views.peliculas, name='peliculas'),
]