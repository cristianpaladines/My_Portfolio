from django.test import TestCase

from .models import Project

class PrimerTest(TestCase):
    def setUp(self):
        Project.objects.create(title="ejemplo", description="ejemplo de descripcion", image="imagen.jpg", url="http://example.com")
        
    def test_modelo(self):
        modelo = Project.objects.get(title="ejemplo")
        self.assertEqual(modelo.description, "ejemplo de descripcion")

