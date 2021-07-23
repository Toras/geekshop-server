from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client

from mainapp.models import Product


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    # заполнение базы для теста
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')
        self.client = Client()

    # чистка файлов после теста, кроме базы
    def tearDown(self):
        pass

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_urls(self):
        for product in Product.objects.all():
            response = self.client.get('/products/#')
            self.assertEqual(response.status_code, self.status_code_success)
