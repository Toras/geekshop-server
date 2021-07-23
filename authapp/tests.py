from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from authapp.models import User


class UserManagementTestCase(TestCase):
    username = 'django'
    email = 'django@dj.ru'
    password = 'pass'
    status_code_success = 200
    status_code_redirect = 302

    new_user_data = {
        'username': 'django',
        'first_name': 'django first',
        'last_name': 'django last',
        'password1': 'pass',
        'password2': 'pass',
        'age': 18,
        'email': 'django@dj.ru'
    }

    def setUp(self):
        self.user = User.objects.create_superuser(self.username, email=self.email, password=self.password)
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.status_code_redirect)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/')
        if response.context['user'].is_authenticated:
            response_logout = self.client.get('/users/logout/')
            self.assertEqual(response_logout.status_code, self.status_code_redirect)

    def test_user_register(self):
        response = self.client.post('/users/register/', data=self.new_user_data)
        self.assertEqual(response.status_code, self.status_code_success)

        new_user = User.objects.get(username=self.new_user_data['username'])
        activate_url = f'{settings.DOMAIN_NAME}/users/verify/{new_user.email}/{new_user.activation_key}/'
        response = self.client.get(activate_url)
        self.assertEqual(response.status_code, self.status_code_success)

        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)
