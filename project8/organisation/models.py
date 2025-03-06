from django.db import models

class org_register(models.Model):
    yourname=models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    access= models.BooleanField(default=False)


class O_details(models.Model):
    name=models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    number = models.CharField(max_length=150)
    city= models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    file = models.FileField(upload_to='files/')
    file2 = models.FileField(upload_to='documents/')
    bool = models.BooleanField(default=False)


class O_purpose(models.Model):
    organisation = models.CharField(max_length=150,null=True)
    type = models.CharField(max_length=150,null=True)
    purpose = models.CharField(max_length=150,null=True)
    quantaity = models.CharField(max_length=150,null=True)
    certified = models.CharField(max_length=150,null=True)
    notcertified = models.CharField(max_length=150,null=True)
    query = models.CharField(max_length=150,null=True)
    boolean=models.BooleanField(default=False)
    boolean1 =models.BooleanField(default=False)
    solutions=models.CharField(max_length=150,null=True)




