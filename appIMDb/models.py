from django.db import models
from decimal import Decimal

class Pelicula(models.Model):
    """Una pelicula con sus caracteristicas y portada."""

    titulo = models.CharField(max_length=100)
    # Considere un limite de 50 caracteres por que los titulos suelen ser cortos, 
    # pero opte por 100 para mantener el nombre original de las peliculas que
    # excedan este numero sin modificar el nombre, como por ej.:
    #   Indiana Jones and the Kingdom of the Crystal Skull (50 caracteres)
    #   Borat: Cultural Learnings of America for Make 
    #       Benefit Glorious Nation of Kazakhstan (83 caracteres)

    anio = models.PositiveSmallIntegerField()
    # El rango de este campo es de 0 a 32767.
    # Adecuado al rango con el que estaremos trabajando (0 a 2XXX)

    sinopsis = models.TextField()

    portada = models.URLField(max_length=200) # Limite por default de Django
    # Uso URLField por que las portadas estaran almacenadas en un servidor externo.

    numVotos = models.PositiveIntegerField()
    # Almacena el numero de usuarios que han calificado la pelicula.

    sumVotos = models.PositiveIntegerField()

    rating = Decimal(sumVotos / numVotos)
    # Obtiene el rating diviediendo la suma de los votos entre el numero de votos.
    # Castea el resultado a Decimal para trabajar con el mas facilmente.

    #POR HACER
    """
    reviews = 
    """
   