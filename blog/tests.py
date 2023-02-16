from django.test import TestCase

from .models import Post

class SegundoTest(TestCase):
    def setUp(self):
        Post.objects.create(title="ejemplo", description="ejemplo de descripcion", image="imagen.jpg", date="16/02/2023")
        
    def test_modelo(self):
        modelo = Post.objects.get(title="ejemplo")
        self.assertEqual(modelo.description, "ejemplo de descripcion")
