from django.db import models

# Create your models here.

class Store(models.Model):
    StoreID = models.AutoField(primary_key=True)
    Store_Name = models.CharField(max_length=50)
    Store_category = models.IntegerField()
    User_ID = models.IntegerField()
    Location = models.CharField(max_length=50)
    Email = models.EmailField(max_length=20)
    Phone = models.CharField(max_length=11)
    Describtion = models.CharField(max_length=500)
