from django.contrib import admin
from .models import  Address, Client


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'zip_code',
        'street',
        'neighborhood',
        'city',
        'state',
        'complement',
    )
    search_fields = ('zip_code', 'street', 'neighborhood', 'city')
    list_filter = ('state',)
    ordering = ('zip_code',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'age',
        'get_formatted_addresses'  
    )
    
    search_fields =('name',)

    def get_formatted_addresses(self, obj):
        
        addresses = obj.addresses.all()
        formatted_addresses = "   |   ".join([f"{address.zip_code} - {address.state}" for address in addresses])
        return formatted_addresses
    
    get_formatted_addresses.short_description = 'Addresses'
    