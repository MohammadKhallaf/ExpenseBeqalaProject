from django.db import models
import product_list.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import *
# Create your models here.
User = get_user_model()
# Create your models here.

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Store(models.Model):
    name = models.CharField(max_length=50)
    category_name = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    user_account = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default="unknown")
    address = models.CharField(max_length=200, default="unknown")
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
        store = models.ForeignKey('store.Store', to_field='id', on_delete=models.CASCADE)
        product = models.ForeignKey(product_list.models.Product, to_field='id', on_delete = models.CASCADE)
        price = models.FloatField()
        offer = models.FloatField()

        def __str__(self):
            return self.price


class ProductOffer(models.Model):
    price = models.ForeignKey(ProductPrice, to_field='id', on_delete = models.CASCADE)
    offer = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.offer       
