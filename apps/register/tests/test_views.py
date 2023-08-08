from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from register.models import Address

class AddressAPITest(APITestCase):
    def test_create_address(self):
        url = reverse('address-list')
        data = {
            'zip_code': '12345-678',
            'street': 'Rua Teste',
            'neighborhood': 'Bairro Teste',
            'city': 'Cidade Teste',
            'state': 'SP',
            'complement': 'Complemento Teste'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().zip_code, '12345-678')

    def test_get_address_by_zip_code(self):
        address = Address.objects.create(
            zip_code='12345-678',
            street='Rua Teste',
            neighborhood='Bairro Teste',
            city='Cidade Teste',
            state='SP',
            complement='Complemento Teste'
        )
        url = reverse('address-zip', args=[address.zip_code])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sucesso'], True)
        self.assertEqual(response.data['endereco']['cep'], '12345-678')

    def test_get_address_by_invalid_zip_code(self):
        url = reverse('address-zip', args=['invalid-zip-code'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['sucesso'], False)