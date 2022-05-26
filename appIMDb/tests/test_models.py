from django.test import TestCase

from appIMDb.models import Pelicula, Genero

class PeliculaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configura objetos no modificados usados por todos los metodos de pruebas.
        Genero.objects.create(nombre='Comedia')
        Pelicula.objects.create(
            titulo='Cindy La Regia', 
            codigo='tt8200456',
            genero=Genero.objects.get(id=1),
            anio=2020,
            sinopsis="When Cindy decides that she doesn't want to marry her boyfriend, she runs to Mexico City, where new friendships and unexpected paths teach her that there are many more possibilities for her life and talent than she thought.",
            portada='https://m.media-amazon.com/images/M/MV5BOWI2MDQ1ODItMjJjNS00MjY5LWJhZmItM2JkNTI0YzQ3OWE1XkEyXkFqcGdeQXVyMzcwOTM4NzY@._V1_.jpg',
            )

    # Pruebas para campo de Titulo

    def testTituloLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('titulo').verbose_name
        self.assertEqual(fieldLabel, 'titulo')

    def testTituloMaxLength(self):
        pelicula = Pelicula.objects.get(id=1)
        maxLength = pelicula._meta.get_field('titulo').max_length
        self.assertEqual(maxLength, 100)

    def testNombreObjectoEsTitulo(self):
        pelicula = Pelicula.objects.get(id=1)
        nombreEsperado = f'{pelicula.titulo}'
        self.assertEqual(str(pelicula), nombreEsperado)

    # Pruebas para campo de Codigo

    def testCodigoLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('codigo').verbose_name
        self.assertEqual(fieldLabel, 'codigo')

    def testCodigoMaxLength(self):
        pelicula = Pelicula.objects.get(id=1)
        maxLength = pelicula._meta.get_field('codigo').max_length
        self.assertEqual(maxLength, 10)

    def testCadenaCodigo(self):
        pelicula = Pelicula.objects.get(id=1)
        codigoEsperado = f'{pelicula.codigo}'
        self.assertEqual(str(pelicula.codigo), codigoEsperado)

    # Pruebas para campo de Genero

    def testGeneroLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('genero').verbose_name
        self.assertEqual(fieldLabel, 'genero')

    def testGeneroMaxLength(self):
        pelicula = Pelicula.objects.get(id=1)
        # Genero es otro objeto, se obtiene el max length de este objeto.
        maxLength = pelicula.genero._meta.get_field('nombre').max_length
        self.assertEqual(maxLength, 50)

    def testCadenaGenero(self):
        pelicula = Pelicula.objects.get(id=1)
        generoEsperado = f'{pelicula.genero}'
        self.assertEqual(str(pelicula.genero), generoEsperado)

    # Pruebas para campo de Anio

    def testAnioLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('anio').verbose_name
        self.assertEqual(fieldLabel, 'anio')

    def testCadenaAnio(self):
        pelicula = Pelicula.objects.get(id=1)
        anioEsperado = f'{pelicula.anio}'
        self.assertEqual(str(pelicula.anio), anioEsperado)

    # Pruebas para campo de Sinopsis

    def testSinopsisLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('sinopsis').verbose_name
        self.assertEqual(fieldLabel, 'sinopsis')

    def testSinopsisMaxLength(self):
        pelicula = Pelicula.objects.get(id=1)
        maxLength = pelicula._meta.get_field('sinopsis').max_length
        self.assertEqual(maxLength, 500)

    def testCadenaSinopsis(self):
        pelicula = Pelicula.objects.get(id=1)
        sinopsisEsperado = f'{pelicula.sinopsis}'
        self.assertEqual(str(pelicula.sinopsis), sinopsisEsperado)

    # Pruebas para campo de Portada

    def testPortadaLabel(self):
        pelicula = Pelicula.objects.get(id=1)
        fieldLabel = pelicula._meta.get_field('portada').verbose_name
        self.assertEqual(fieldLabel, 'portada')

    def testPortadaMaxLength(self):
        pelicula = Pelicula.objects.get(id=1)
        maxLength = pelicula._meta.get_field('portada').max_length
        self.assertEqual(maxLength, 200)

    def testCadenaPortada(self):
        pelicula = Pelicula.objects.get(id=1)
        portadaEsperado = f'{pelicula.portada}'
        self.assertEqual(str(pelicula.portada), portadaEsperado)

    # Prueba para nombre plural

    def testPluralName(self):
        pelicula = Pelicula.objects.get(id=1)
        pluralEsperado = pelicula._meta.verbose_name_plural
        self.assertEqual(str(pelicula._meta.verbose_name_plural), pluralEsperado)
"""
class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""
