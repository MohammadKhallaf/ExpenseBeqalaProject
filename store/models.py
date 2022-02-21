from django.db import models
from accounts.models import UserAccount
import product_list.models

# Create your models here.

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Location(models.Model):
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    describe = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.city} - {self.region}"
=======
>>>>>>> cc601ec8e6c91dc5c6466a4b372e0ad98fb9f64e


class Store(models.Model):
    name = models.CharField(max_length=50)
    category_name = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    user_account = models.ForeignKey(UserAccount, to_field='id', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default="unknown")
    address = models.CharField(max_length=200, default="unknown")
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=11)
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
