from django.db import models

# Create your models here.
class AccountInfo(models.Model):
    acno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    gender= models.CharField(max_length=6)
    address= models.TextField()
    dob= models.CharField(max_length=30)
    contactno = models.IntegerField()
    emailaddress= models.EmailField(max_length=50)
    panno= models.CharField(max_length=10)
    aadharno= models.CharField(max_length=12)
    balance= models.IntegerField()
    password = models.CharField(max_length =20)
    openingdate=models.CharField(max_length=30)