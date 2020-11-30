from django.test import TestCase
from dotgames.models import Genero

class GeneroModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genero.objects.create(nombre='prueba')

    def test_nombre_label(self):
        nombre= Genero.objects.get(id=1)
        field_label = nombre._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')