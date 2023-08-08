from django.urls import path
from .views import (
    AddressAPIView, 
    AdressesAPIView, 
    AddressDetailView,
    ClientAPIView,
    ClientsAPIView,
    ClientAddressesAPIView,
    )

urlpatterns = [
    path('address/', AddressAPIView.as_view(), name = 'address'),
    path('address/<int:pk>/', AdressesAPIView.as_view(), name = 'addresses'),
    path('address/zip/<str:zip_code>/', AddressDetailView.as_view(), name='address-zip'),
    
    path('client/', ClientAPIView.as_view(), name = 'client'),
    path('client/<int:pk>/', ClientsAPIView.as_view(), name = 'clients'),
    
    path('client/<int:client_pk>/address/', ClientAddressesAPIView.as_view(), name = 'client-addresses'),
    
]