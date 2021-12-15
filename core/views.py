from rest_framework import viewsets
from core.models import Empresa,Endereco,Cliente,Contrato,NotaPromissoria
from core.serializer import EmpresaSerializer, EnderecoSerializer, ClienteSerializer, ContratoSerializer, NotaPromissoriaSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as empresas"""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os enderecos"""
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer