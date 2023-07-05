from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

import shutil
import os


class RegisterTest(APITestCase):
    
    def setUp(self):
        client = APIClient()
        self.user_1 = get_user_model().objects.create_user(id=1, username='valera_55', first_name='blue', email='valera949494@gmail.com', password='3_Q+val73_qwerty', gender='M', avatar='app/test.jpg')
        # self.token = Token.objects.create(user=self.user_1)
        self.token = Token.objects.get_or_create(user=self.user_1)

    def test_register(self):
        file = open('app/test_avatar.jpg', 'rb')
        client = APIClient()
        payload = {'username': 'valera_2_test', 'first_name': 'Valeriu', 'password': '3_Q+val73_qwerty', 'email': 'email@gmail.com', 'gender': 'M', 'avatar': file}
        response = self.client.post('http://localhost:8000/api/clients/create/', data=payload, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(get_user_model().objects.count(), 2)
        shutil.rmtree('images/valera_2_test')
        

    def test_all_users(self):
        # self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token[0]))
        response = self.client.get(reverse('search'), data={'gender': 'M'})
        self.assertEqual(response.status_code, 200)

