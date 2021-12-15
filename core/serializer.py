from rest_framework import serializers
from core.models import Empresa,Endereco,Cliente,Contrato,NotaPromissoria

## A classe serializer faz a ponte do ORM do django com o formato JSON ##

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'


class NotaPromissoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPromissoria
        fields = '__all__'
