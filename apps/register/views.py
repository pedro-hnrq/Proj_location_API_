from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Address, Client
from .serializers import AddressSerializer, ClientSerializer

from utils.viacep import get_address_info_by_cep

"""
API V1
"""

class AddressAPIView(generics.ListCreateAPIView):
    """
    API de Endereço
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "sucesso": True,
                "endereco": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdressesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetailView(APIView):
    def get(self, request, *args, **kwargs):
        zip_code = self.kwargs.get('zip_code')
        address_info = get_address_info_by_cep(zip_code)

        if address_info:
            return Response({"sucesso": True, "endereco": address_info})
        else:
            return Response({"sucesso": False, "mensagem": "CEP não encontrado"}, status=400)
        

class ClientAPIView(generics.ListCreateAPIView):
    """
    API de Clientes
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientAddressesAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def get_queryset(self):
        if self.kwargs.get('client_pk'):
            return self.queryset.filter(clients__id=self.kwargs.get('client_pk'))
        return self.queryset.all() 



"""
API V2
"""