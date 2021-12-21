from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Endereco(models.Model):

    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=25)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=155)
    estado = models.CharField(max_length=155)
    bairro = models.CharField(max_length=155)
    complemento = models.CharField(max_length=155)

    def __str__(self):
        return self.logradouro


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Contrato(models.Model):
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor_total = models.FloatField()
    qtd_nota_promissoria = models.IntegerField()

    def __str__(self):
        return self.descricao


class NotaPromissoria(models.Model):
    contrato_id = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        self = 'salvo'
        return self
