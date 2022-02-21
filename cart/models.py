from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import *
# Create your models here.
User = get_user_model()
class CheckOut(models.Model):
    # orderID is Django id
    # StoreID 
    # orderDate updated when done checkout
    STATE_CHOICES = (
    ('open','OPEN'),
    ('pending', 'PENDING'),
    ('done','DONE'),
    )
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    store = models.IntegerField()
    orderDate = models.DateTimeField(null=True)
    state = models.CharField(max_length=8, choices=STATE_CHOICES, default='open')
    def __str__(self):
        return f"{self.user} - {self.store} - {self.id}"
class Cart(models.Model):
   
    #productID
    order = models.ForeignKey(CheckOut, on_delete=models.CASCADE, related_name='carts')
    product = models.IntegerField()
    quantity = models.PositiveIntegerField()
    price =  models.FloatField()

    def __str__(self):
        return f"{self.order} - {self.product} - {self.quantity}"

