from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from users.models import User

TEST_PASSWORD = '1234'
LOGIN_URL = reverse('users:login')
UPDATE_PASSWORD_URL = reverse('users:password_update')


class UserTests(APITestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='test', password=TEST_PASSWORD, email='test@email.com')

    def test_login_valid(self):
        user = User.objects.get(username='test')
        data = {
            'username': user.username,
            'password': TEST_PASSWORD,
        }
        response = self.client.post(LOGIN_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_unknown_username(self):
        data = {
            'username': 'bad_user',
            'password': TEST_PASSWORD,
        }
        response = self.client.post(LOGIN_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertRaises(AuthenticationFailed, msg='No active account found with the given credentials')

    def test_login_wrong_password(self):
        user = User.objects.get(username='test')
        data = {
            'username': user.username,
            'password': 'random_password',
        }
        response = self.client.post(LOGIN_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertRaises(AuthenticationFailed, msg='No active account found with the given credentials')
