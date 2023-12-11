from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTest(TestCase):
    def testProduct(self):
        product = Product(title="My Product", content="My first product", price=100.00)
        self.assertEqual(product.public, True)
        self.assertEqual(product.title, "My Product")
        self.assertEqual(product.content, "My first product")
        self.assertEqual(product.price, 100.00)
