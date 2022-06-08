from django.db import models


class Pedidos(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    telephone = models.IntegerField()
    respuesto = models.CharField(max_length=40)


class Stock(models.Model):
    respuesto = models.CharField(max_length=40)



class Cliente(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    cuit = models.IntegerField()


class Envios(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    adress = models.CharField(max_length=40)
    telephone = models.IntegerField()
    code_postal = models.IntegerField()
    due_date = models.DateField()
    is_delivered = models.BooleanField()
