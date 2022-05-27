# Clon IMDb creado con Django
Esta WebApp que cumple con las siguientes caracteristicas:
* **Mostrar un listado de peliculas por genero**:
    El usuario selecciona  un genero del que le gustaria ver todas  las peliculas disponibles, y se muestra un  listado con estas peliculas. Cada una es un link para entrar a la pagina de detalles individual.
* **Pagina que muestra los detalles de una pelicula**:
    En esta pagina, el usuario podra observar los diferentes campos que contiene una pelicula, como lo son:
    1. Titulo
    2. Anio de lanzamiento
    3. Sinopsis
    4. Portada
    5. Reviews
    6. Rating
    Este es calculado en base a las reviews de los usuarios.
    7. Codigo IMDb
    Este ultimo  hace referencia al id unico que IMDb otorga a cada pelicula.

* **Funcion de reviews y calificaciones**:
Los usuarios  pueden  dejar reviews y calificaciones a  las peliculas que deseen.
Cada review viene acompaniada de una calificacion del 1 al 10. Los usuarios solo pueden dejar un review/calificacion por pelicula.
Esta funcion de reviews tambien incluye la funcion de editar algun review realizado anteriormente, asi como eliminar la review que hallan hecho.
* **Funcion de favoritos**:
Los usuarios pueden marcar pueden agregar (y eliminar de) las peliculas que gusten a su lista de favoritos, asimismo, pueden accesar esta lista y visualizar las peliculas que han marcado como favoritas.

---
# Documentacion

## Modelos

Empezare explicando los principales modelos que componen a la aplicacion.

El archivo se puede encontrar en: appIMDb/models.py
En los comentarios dentro de este archivo podran encontrar explicaciones mas detalladas sobre las decisiones de disenio que tome.

## Genero
>
>Este modelo cuenta con un solo campo:
> * **Nombre**:
>Almacena una cadena con el nombre del genero.
>Tiene un limite maximo de 50 caracteres.
>
>Nombre plural: _generos_
>
>La representacion que este modelo regresa es el nombre del Genero en una cadena.

## Pelicula
>
>Este modelo cuenta con los siguientes campos:
> * **Titulo**:
>Almacena una cadena con el titulo de la pelicula.
>Tiene un limite maximo de 100 caracteres.
>Es unico.
>
>* **Codigo**:
>El ID otorgado por IMDb a esta pelicula.
>Tiene un limite maximo de 10 caracteres.
>Es unico.
>
>* **Genero**:
>Este campo es una relacion ForeignKey al modelo Genero.
>Cada pelicula solo puede estar conectada a un objeto de Genero.
>
>* **Anio**:
>Almacena un numero entero mayor a 0.
>Representa el anio de lanzamiento de la pelicula.
>
>* **Sinopsis**:
>Almacena un texto en cadena que representa la sinopsis de la Pelicula.
>Tiene un limite maximo de 500 caracteres.
>
>* **Portada**:
>Este campo almacena una URL, que dirige a donde hosteada la portada de la pelicula.
>Tiene un limite maximo de 200 caracteres, el limite por default de Django.
>
>* **Favoritos**:
>Este campo es una relacion ManyToMany.
>Vincula los ID's de los usuarios que han marcado la Pelicula como favorita.
>
>Nombre plural: _peliculas_
>
>La representacion que este modelo regresa es el titulo de la Pelicula en una cadena.
>En caso de que la longitud de la cadena Titulo supere los 50 caracteres, se muestra hasta el caracter 50, seguido de tres puntos suspensivos (...).

## Review
>
>Este modelo cuenta con los siguientes campos:
> * **Usuario**:
>Este campo es una relacion ForeignKey, vinculada a un usuario.
>Una review solo puede estar vinculada a un usuario.
>Se usa el atributo on_delete=models.CASCADE; si el usuario vinculado a un review es eliminado, todas sus reviews tambien seran eliminadas.
>
>* **Pelicula**:
>Este campo es una relacion ForeignKey, vinculada a un objeto Pelicula.
>Una review solo puede estar vinculada a una Pelicula.
>Se usa el atributo on_delete=models.CASCADE; si la pelicula vinculada a un review es eliminada, todas sus reviews tambien seran eliminadas.
>
>* **Texto**:
>Este es un campo de texto que almacena la la cadena que el usuario escribe como review.
>Se usa el atributo null=True, en caso que el usuario solo desee dejar su calificacion pero no quiera escribir un review.
>
>* **Calificacion**:
>Este campo almacena un numero entero, que sea mayor o igual a 0, y menor o igual a 10.
>Se elige este rango debido a que permite dos tipos de visualizaciones de calificaciones.
>Permite mostrar una calificacion del 1 al 10, y permitiria mostrar una representacion de la calificacion en "5 estrellas". 
>Mas detalles y explicacion en el archivo appIMDb/models.py
>
>* **Fecha**:
>Este campo almacena la fecha en que la review fue realizada.
>La fecha se agrega en automatico; sirve para ordenar las reviews al momento de visualizarlas.
>
>Nombre plural: _reviews_
>
>La representacion que este modelo regresa sigue la siguiente forma:
>`Usuario: Texto`
>En caso que la longitud de la cadena de Texto de la review supere los 50 caracteres, se muestran los primeros 50 caracteres del Texto, seguido de 3 puntos suspensivos. 
