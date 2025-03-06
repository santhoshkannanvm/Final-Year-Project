from django.db import models



class admin_rqst(models.Model):
    organisation = models.CharField(max_length=150, unique=True)
    amount = models.CharField(max_length=150)
