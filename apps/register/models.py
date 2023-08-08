from django.db import models
import re
from .choices import ChoiceUF

from utils.viacep import get_address_info_by_cep
from utils.validators import (validate_zip_code, 
                              validate_state, 
                              validate_name, 
                              validate_full_name, 
                              validate_age)

class Address(models.Model):
    
      
    zip_code = models.CharField(max_length=9, validators=[validate_zip_code])  # CEP com 9 dígitos (formato: 'XXXXX-XXX' ou 'XXXXXXXX')
    street = models.CharField(max_length=200)  # logradouro
    neighborhood = models.CharField(max_length=100)  # bairro
    city = models.CharField(max_length=100)  # cidade
    state = models.CharField(max_length=2, choices=ChoiceUF.choices, validators=[validate_state])  # Estado=UF
    complement = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        
    def __str__(self):
        return f'CEP: {self.zip_code} - {self.street}'
    
    def save(self, *args, **kwargs):
        if self.zip_code:
            # Remove qualquer caractere não numérico do CEP
            self.zip_code = re.sub(r'\D', '', self.zip_code)
            # Formata o CEP adicionando o traço '-' se necessário
            if len(self.zip_code) == 8:
                self.zip_code = f'{self.zip_code[:5]}-{self.zip_code[5:]}'
            
            address_info = get_address_info_by_cep(self.zip_code)
            if address_info:
                self.street = address_info['logradouro']
                self.neighborhood = address_info['bairro']
                self.city = address_info['cidade']
                self.complement = address_info['complemento']
                self.state = address_info['uf']
        super(Address, self).save(*args, **kwargs)


class Client(models.Model):
    name = models.CharField(max_length=150, validators=[validate_name, validate_full_name])  # nome
    age = models.IntegerField(validators=[validate_age])  # Idade
    addresses = models.ManyToManyField(Address, blank=True, related_name='clients')
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'Nome: {self.name} - Idade: {self.age} anos'
    
    