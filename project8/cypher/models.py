from django.db import models

class cypher_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)


class cypher_admin_update(models.Model):
    name=models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    adminfile = models.FileField(upload_to='documents/')