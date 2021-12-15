from django.contrib import admin
from core.models import Empresa, Endereco, Cliente, Contrato, NotaPromissoria

class Empresas(admin.ModelAdmin):
    #List Display são as informacoes que disponibilizamos na API
    list_display = ('id','nome','cnpj')
    #List Display Link sao informacoes para quando formos
    # alterar uma informacao, na linha abaixo poderiamos alterar
    # a empresa pelo id ou pelo nome
    list_display_links = ('id', 'nome')
    #Search Field são os campos em que podemos fazer a busca da classe
    search_fields = ('nome', 'cnpj')

#Aqui é onde registramos a configuração no admin do django
admin.site.register(Empresa, Empresas)

class Enderecos(admin.ModelAdmin):
    list_display = ('id','logradouro','numero','cep','cidade','estado','bairro','complemento')
    list_display_links = ('id','logradouro')
    search_fields = ('id','logradouro')

admin.site.register(Endereco,Enderecos)

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','telefone','endereco_id')
    list_display_links = ('id','nome','cpf')
    search_fields = ('id','nome','cpf')

admin.site.register(Cliente,Clientes)

class Contratos(admin.ModelAdmin):
    list_display = ('id','descricao','valor_total','qtd_nota_promissoria','empresa_id','cliente_id')
    list_display_links = ('id','descricao')
    search_fields = ('id','valor','cliente_id')

admin.site.register(Contrato,Contratos)

class NotasPromissorias(admin.ModelAdmin):
    list_display = ('id','contrato_id','valor','data_vencimento')
    list_display_links = ('id','contrato_id','valor','data_vencimento')
    search_fields = ('id','contrato_id','valor','data_vencimento')

admin.site.register(NotaPromissoria,NotasPromissorias)
