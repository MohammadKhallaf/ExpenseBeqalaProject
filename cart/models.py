from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import *
# Create your models here.
User = get_user_model()
class CheckOut(models.Model):
    # orderID is Django id
    # StoreID 
    userID = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    storeID = models.IntegerField()
    orderDate = models.DateTimeField()
    
    def __str__(self):
        return self.userID

class Cart(models.Model):
   
    #productID
    orderID = models.ForeignKey(CheckOut, on_delete=models.CASCADE, related_name='cart_user')
    productID = models.IntegerField()
    quantity = models.PositiveIntegerField()
    price =  models.FloatField()

    def __str__(self):
        return self.userID

