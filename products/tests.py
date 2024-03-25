from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Enterprise

class EnterpriseTests(APITestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(
            name='Test Enterprise',
            description='Test Description',
            location='Test Location',
            opening_hours='08:00',
            closing_hours='18:00',
            is_24_7=False
        )

    def test_get_enterprise_list(self):
        url = reverse('enterprise-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.enterprise.name)

    def test_create_enterprise(self):
        url = reverse('enterprise-list')
        data = {
            'name': 'New Enterprise',
            'description': 'New Description',
            'location': 'New Location',
            'opening_hours': '09:00',
            'closing_hours': '17:00',
            'is_24_7': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Enterprise.objects.count(), 2)