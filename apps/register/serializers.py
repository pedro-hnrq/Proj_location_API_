from rest_framework import serializers

from .models import Address, Client

from utils.viacep import get_address_info_by_cep
from utils.validators import (validate_zip_code, 
                              validate_state, 
                              validate_name, 
                              validate_full_name, 
                              validate_age)

class AddressSerializer(serializers.ModelSerializer):
    zip_code = serializers.CharField(validators=[validate_zip_code]) 

    class Meta:
        model = Address
        fields = (
            'id',
            'zip_code',
            'street',
            'neighborhood',
            'city',
            'state',
            'complement'
        )

    def validate_zip_code(self, value):
        value = validate_zip_code(value) 
        return value

    def create(self, validated_data):
        zip_code = validated_data.get('zip_code')
        address_info = get_address_info_by_cep(zip_code)

        if not address_info:
            raise serializers.ValidationError("CEP não encontrado")

        validated_data['street'] = address_info['logradouro']
        validated_data['neighborhood'] = address_info['bairro']
        validated_data['city'] = address_info['cidade']
        validated_data['complement'] = address_info['complemento']
        validated_data['state'] = address_info['uf']

        return super(AddressSerializer, self).create(validated_data)

    
    
    
class ClientSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    
    class Meta: 
        model = Client
        fields = (
            'id',
            'name',
            'age',
            'addresses',
                        
        )
    
    def validate_name(self, value):
        validate_name(value)  
        return value
    
    def validate_full_name(self, value):
        validate_full_name(value)  
        return value

    def validate_age(self, value):
        validate_age(value)  
        return value
    
    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])  
        client = Client.objects.create(**validated_data)

        for address_data in addresses_data:
            Address.objects.create(client=client, **address_data)

        return client

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('addresses', [])  

        for address_data in addresses_data:
            address_id = address_data.get('id', None)
            if address_id:
                address = Address.objects.get(id=address_id, client=instance)
                AddressSerializer().update(address, address_data)
            else:
                Address.objects.create(client=instance, **address_data)

        return super(ClientSerializer, self).update(instance, validated_data)
