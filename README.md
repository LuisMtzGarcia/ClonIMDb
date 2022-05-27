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

### Genero
>
>Este modelo cuenta con un solo campo:
> * **Nombre**:
>Almacena una cadena con el nombre del genero.
>Tiene un limite maximo de 50 caracteres.
>
>Nombre plural: _generos_
>
>La representacion que este modelo regresa es el nombre del Genero en una cadena.

### Pelicula
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

### Review
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

---

## Views

Documentacion de las principales Views utilizadas por la app.
Este archivo se encuentra en appIMDb/views.py
En este, podran encontrar informacion y explicaciones mas detalladas de las aqui presentadas.

### Index
> Funcion estandar, muestra el homepage de la aplicacion.

### Peliculas
> Esta View hace un Query de todas los objetos Pelicula registrados y los ordena por el campo 'titulo'.
> Pasa este QuerySet al template peliculas.html, el cual muestra un listado de todos los objetos Pelicula.

### Pelicula
> La funcion de esta View es recibir un ID de un objeto Pelicula, y pasar este objeto al template, para que muestre toda la informacion de esta.
> Esta View recibe el parametro `pelicula_id`, el cual almacena el ID de una pelicula.
> 1. Recupera el objeto Pelicula que cuente con el mismo ID almacenado en `pelicula_id`
> 2. Hace un Query por todos los objetos Review vinculadas a la Pelicula. Ordenados por fecha.
> 3. En base al QuerySet de las Reviews, obtiene la calificacion promedio.
> 3a. En caso de que el QuerySet este vacio (no existan Reviews), la calificacion se representa como un valor `None`.
> 4. Verifica si el Usuario que esta haciendo el request ha marcado (o no) la Pelicula como favorita. Se almacena un valor `True` o `False` en la variable `favFlag`.
> 5. Se pasa el objeto Pelicula, el QuerySet de Reviews, la calificacion y la `favFlag` al template pelicula.html

### Generos
> Esta view hace un Query de todos los objetos Genero registrados.
> Pasa este QuerySet al template generos.html, el cual muestra un listado de todos los objetos Genero.

### Genero
> La funcion de esta View es recibir un ID de un objeto Genero, y pasar este objeto junto a todas las Peliculas vinculadas a este al template.
> Esta View recibe el parametro `genero_id`, el cual almacena el ID de una pelicula.
> 1. Recupera el objeto Genero que cuente con el mismo ID almacenado en `genero_id`
> 2. Hace un Query por todos los objetos Pelicula vinculados al Genero. Ordenados por titulo.
> 3. Se pasa el objeto Genero y el QuerySet de Peliculas al template genero.html.

### NuevaReview
> La funcion de esta View es almacenar una nueva Review realizada por el usuario.
> Esta View recibe el parametro `pelicula_id`, el cual almacena el ID de una pelicula.
> 1. Recupera el objeto Pelicula que cuente con el mismo ID almacenado en `pelicula_id`
> 2. Filtra las Reviews del objeto Pelicula previamente recuperado usando al Usuario como filtro.
> 2a. Si se encuentra un Review previo del Usuario hacia esta Pelicula, se redirecciona al view `editarReview` y se pasa el ID de la Review encontrada.
> 3. Se genera un formulario en base a `ReviewForm` y, si la informacion es valida, se almacena y crea un nuevo objeto Review.
> 4. Una vez generado y almacenado, se redirecciona al view `pelicula` con el ID del objeto Pelicula recuperado anteriormente.
> Este view pasa el objeto Pelicula y el formulario al template nuevaReview.html

### EditarReview
> La funcion de esta View es editar una Review previamente realizada.
> Se llega a esta View cuando el usuario trata de realizar una nueva Review a una pelicula que previamente ha hecho un Review.
> Esta View recibe el parametro `review_id`, el cual almacena el ID de una Review.
> 1. Recupera el objeto Review que cuente con el mismo ID almacenado en `review_id`
> 2. Verifica que el usuario que esta accediendo a esta View sea el propietario de la Review recuperada.
> 3. Se genera un formulario en base a `ReviewForm`, rellena los datos de este con los datos de la Review recuperada.
> 4. Una vez almacenados los cambios, se redirecciona al view `pelicula` con el ID del objeto Pelicula al cual la Review esta vinculada.
>Este View pasa el objeto Review y Pelicula, junto con el formulario, al template editarReview.html

### BorrarReview
> La funcion de esta View es eliminar una Review previamente realizada.
> Esta View recibe el parametro `review_id`, el cual almacena el ID de una Review.
> 1. Recupera el objeto Review que cuente con el mismo ID almacenado en `review_id`
> 2. Recupera el objeto Pelicula al que la Review esta vinculada
> 3. Verifica que el usuario que esta haciendo el request sea el propietario de la Review.
> 4. Si asi es, elimina la Review y redireccionna al view `pelicula` con el ID del objeto Pelicula previamente recuperado.
> 4a. De no ser asi, se levanta `PermissionDenied`
> No cuenta con un template.