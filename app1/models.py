from django.db import models

class AdminLoginModel(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=30)


class StockerModel(models.Model):
    idno = models.IntegerField()
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(max_length=10,unique=True)
    password = models.CharField(max_length=30)


class AddDispatcherModel(models.Model):
    idno = models.IntegerField()
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(max_length=10,unique=True)
    password = models.CharField(max_length=30)