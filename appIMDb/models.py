from django.db import models
from decimal import Decimal

class Pelicula(models.Model):
    """Una pelicula con sus caracteristicas y portada."""

    titulo = models.CharField(max_length=100, unique=True)
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

    def __str__(self):
        """Regresa una representacion en cadena del 'titulo' del modelo."""

        return self.titulo


class Review(models.Model):
    """Una review de un usuario para una pelicula."""

    usuario = models.CharField(max_length=50) 
    # Placeholder en lo que aniado los usuarios.

    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    texto = models.TextField()
    # No tiene un limite actual, pero considerare un limite.

    def __str__(self):
        """Regresa una representacion en cadena de la review."""

        # En caso de que la review supere los 100 caracteres, aniade 
        # puntos suspensivos.
        if len(self.texto > 100):
            return f"{self.usuario}: {self.texto[:100]}..."
        else:
            return f"{self.usuario}: {self.texto}"
   
class Rating(models.Model):
    """Un voto realizado por un usuario."""

    usuario = models.CharField(max_length=50)
    # Placeholder en lo que aniado los usuarios.

    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    calificacion = models.PositiveSmallIntegerField()
    # Votos del 1 al 10
    # Se elige este rango por que funciona para dos tipos de visualizacion:
    #       - Una calificacion del 1 al 10
    #       - Una representacion en 'estrellas', de 1 a 5.
    #       Ejemplo:
    #           Calificacion: 8
    #               Representacion 1 a 10: 8
    #               Representacion estrellas: 4
    #                   - Se divide la calificacion en 2, 
    #       Tambien, permite la representacion de medias estrellas:
    #               Representacion 1 a 10: 9
    #               Representacion estrellas: 4.5 ( 9 / 2 = 4.5 )
    #
    # Asimismo, si redondeamos el resultado de dividir la calificacion base10,
    # se podria redondear a las representaciones adecuadas en estrellas.
    # Ejemplo:
    #       Repr. 1 a 10: 6.8
    #           (6.8 / 2 = 3.4)
    #       Repr. estrellas: 3.5 o 3

    def __str__(self):
        """Regresa una representacion en cadena del rating."""

        return f"{self.usuario} da un {self.calificacion} a {self.pelicula}"