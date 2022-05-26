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
