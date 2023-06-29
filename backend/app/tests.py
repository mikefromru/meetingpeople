from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(id=1, username='valera_1', password='3_Q+val73_qwerty')
        self.token = Token.objects.create(user=self.user)

    def test_register(self):
        file = open('app/test_avatar.jpeg', 'rb')
        client = APIClient()
        payload = {'username': 'valera_2', 'first_name': 'Valeriu', 'password': '3_Q+val73_qwerty', 'email': 'email@gmail.com', 'gender': 'M', 'avatar': file}
        response = self.client.post('http://localhost:8000/api/clients/create/', data=payload, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(get_user_model().objects.count(), 2)