from django.db import models
# from decimal import *
# Create your models here.

class Usuarios(models.Model):

    number = models.IntegerField()

    nome = models.CharField(
        max_length=200,
    )

class Number(models.Model):

    id = models.IntegerField(primary_key=True)

class Conta(models.Model):

    BANCHO_CHOICES = [
        ('Santander', 'Santander'),
        ('BB', 'Banco do Brasil'),
        ('ITAU','ITAU'), 
    ]
    
    number = models.IntegerField()

    banco = models.CharField(
        choices=BANCHO_CHOICES,
        max_length=200
    )


    money_in_account = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

class Gastos(models.Model):

    descricao_gasto = models.CharField(max_length=200)


    date = models.DateField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null="True"
    )

    number = number = models.IntegerField()