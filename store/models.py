from django.db import models
from accounts.models import UserAccount
import product_list.models

# Create your models here.

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Location(models.Model):
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    describe = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.city} - {self.region}"


class Store(models.Model):
    name = models.CharField(max_length=50)
    category_name = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    user_account = models.ForeignKey(UserAccount, to_field='id', on_delete=models.CASCADE)
    products = models.ManyToManyField('product_list.Product', through='ProductPrice')
    location = models.ForeignKey(Location, to_field='id', on_delete=models.CASCADE, related_name='storeLocation')
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=11)
    describtion = models.CharField(max_length=500)



    def __str__(self):
        return self.name



class ProductPrice(models.Model):
        store = models.ForeignKey('store.Store', to_field='id', on_delete=models.CASCADE)
        product = models.ForeignKey(product_list.models.Product, to_field='id', on_delete = models.CASCADE)
        price = models.FloatField()
        offer = models.FloatField()

        def __str__(self):
            return self.price
