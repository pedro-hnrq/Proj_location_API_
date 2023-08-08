from django.test import TestCase
from register.models import Address, Client

class AddressModelTest(TestCase):
    def test_address_creation(self):
        address = Address.objects.create(
            zip_code='12345-678',
            street='Rua Teste',
            neighborhood='Bairro Teste',
            city='Cidade Teste',
            state='SP',
            complement='Complemento Teste'
        )
        self.assertEqual(address.zip_code, '12345-678')
        self.assertEqual(address.street, 'Rua Teste')
        self.assertEqual(address.neighborhood, 'Bairro Teste')
        self.assertEqual(address.city, 'Cidade Teste')
        self.assertEqual(address.state, 'SP')
        self.assertEqual(address.complement, 'Complemento Teste')

class ClientModelTest(TestCase):
    def test_client_creation(self):
        client = Client.objects.create(
            name='João da Silva',
            age=30
        )
        self.assertEqual(client.name, 'João da Silva')
        self.assertEqual(client.age, 30)