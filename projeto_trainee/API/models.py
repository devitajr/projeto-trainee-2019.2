from django.db import models
# from decimal import *
# Create your models here.

class Usuarios(models.Model):

    username = models.CharField(
        unique=True,
        max_length=200
    )

    password = models.CharField(
        max_length=200
    )

    number = models.IntegerField(
        primary_key=True
    )

    email = models.EmailField(
        max_length=200
    )

class Conta(models.Model):

    BANCHO_CHOICES = [
        ('Santander', 'Santander'),
        ('BB', 'Banco do Brasil'),
        ('ITAU','ITAU') 
    ]
    
    number = models.ForeignKey(
        'Usuarios',
        on_delete = models.DO_NOTHING
    )

    banco = models.CharField(
        choices=BANCHO_CHOICES,
        max_length=200
    )


    money_in_account = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    id_conta = models.IntegerField(primary_key=True)

class Gastos(models.Model):

    descricao_gasto = models.CharField(max_length=200)


    date = models.DateField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null="True"
    )

    number = number = models.ForeignKey(
        'Usuarios',
        on_delete = models.DO_NOTHING
    )

    id_gastos = models.IntegerField(primary_key=True)