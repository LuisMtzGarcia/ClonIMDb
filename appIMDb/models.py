from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    """Un genero de pelicula."""

    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'generos'

    def __str__(self):
        """Devuelve una representacion en cadena del genero."""

        return f"{self.nombre}"

class Pelicula(models.Model):
    """Una pelicula con sus caracteristicas y portada."""

    titulo = models.CharField(max_length=100, unique=True)
    # Considere un limite de 50 caracteres por que los titulos suelen ser cortos, 
    # pero opte por 100 para mantener el nombre original de las peliculas que
    # excedan este numero sin modificar el nombre, como por ej.:
    #   Indiana Jones and the Kingdom of the Crystal Skull (50 caracteres)
    #   Borat: Cultural Learnings of America for Make 
    #       Benefit Glorious Nation of Kazakhstan (83 caracteres)

    codigo = models.CharField(max_length=10, unique=True)
    # IMDb le otorga un codigo de 9 caracteres a todas las peliculas en su base de datos.
    # Este codigo funciona para encontrar mas informacion sobre una pelicula,
    # ignorando el lenguaje del idioma y eliminando la necesidad de 'adivinar'
    # el nombre de la pelicula en otro idioma.
    # Ejemplos de diferentes casos:
    #   - El mejor de los casos:
    #       Nombre original: "Iron Man"
    #       Nombre espaniol: "Iron Man"
    #       
    #       En este caso, el titulo original de la pelicula es el mismo en todo el 
    #       mundo.
    #
    #   - El titulo es traducido literalmente:
    #       Nombre original: "Legally Blonde"
    #       Nombre espaniol: "Legalmente Rubia"
    #
    #       En estos casos, el titulo original es traducido y podemos encontrar mas
    #       informacion de la pelicula solo asumiendo que se traduce el nombre.
    #
    #   - El titulo es completamente diferente:
    #       Nombre original: "John Wick"
    #       Nombre espaniol: "Otro dia para matar"
    #       
    #       En estos casos, el titulo es completamente diferente, ya sea por razones
    #       de marketing o por que el nombre viene de una lengua con un alfabeto
    #       diferente.

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    # Cada pelicula solo puede tener un genero.

    anio = models.PositiveSmallIntegerField()
    # El rango de este campo es de 0 a 32767.
    # Adecuado al rango con el que estaremos trabajando (0 a 2XXX)

    sinopsis = models.TextField()

    portada = models.URLField(max_length=200) # Limite por default de Django
    # Uso URLField por que las portadas estaran almacenadas en un servidor externo.

    class Meta:
        verbose_name_plural = 'peliculas'

    def __str__(self):
        """Regresa una representacion en cadena del 'titulo' del modelo."""

        if len(self.titulo) > 50:
            return f"{self.titulo[:50]}..."
        else:
            return f"{self.titulo}"


class Review(models.Model):
    """Una review de un usuario para una pelicula."""

    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)

    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    texto = models.TextField(null=True)
    # No tiene un limite actual, pero considerare un limite.

    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        """Regresa una representacion en cadena de la review."""

        # En caso de que la review supere los 50 caracteres, aniade 
        # puntos suspensivos.
        if len(self.texto) > 50:
            return f"{self.usuario}: {self.texto[:50]}..."
        else:
            return f"{self.usuario}: {self.texto}"
   
class Rating(models.Model):
    """Un voto realizado por un usuario."""

    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)

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