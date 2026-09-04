from django.test import TestCase

from .models import Categoria, Producto


class ProductoModelTests(TestCase):
    def test_producto_usa_categoria(self):
        categoria = Categoria.objects.create(nombre='Herramientas')
        producto = Producto.objects.create(
            nombre='Martillo',
            precio='12.50',
            categoria=categoria,
        )

        self.assertEqual(producto.categoria.nombre, 'Herramientas')