from django.db import models

class process_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)

class r_isotope(models.Model):
    team=models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    result = models.CharField(max_length=150)
    solution = models.CharField(max_length=150, null=True)
