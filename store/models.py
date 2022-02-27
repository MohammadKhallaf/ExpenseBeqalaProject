from django.db import models
import product_list.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
User = get_user_model()

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Store(models.Model):
    STATE_CITY = (
        ('cairo', 'CAIRO'),
        ('alex', 'ALEXANDRIA')
    )
    name = models.CharField(max_length=50)
    category_name = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    user_account = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, choices=STATE_CITY, default="cairo")
    address = models.CharField(max_length=200, default="unknown")
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=14)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id} - {self.user_account} - {self.city}"

class ProductPrice(models.Model):
    store = models.ForeignKey('store.Store', to_field='id', on_delete=models.CASCADE)
    product = models.ForeignKey(product_list.models.Product, to_field='id', on_delete=models.CASCADE)
    price = models.FloatField()
    

    def __str__(self):
        return f"{self.store} - {self.product} - {self.price}"

class ProductOffer(models.Model):
    price = models.ForeignKey(ProductPrice, to_field='id', on_delete=models.CASCADE)
    offer = models.FloatField(validators=[MaxValueValidator(99.9), MinValueValidator(1)])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.offer} - {self.price} - {self.start_date}- {self.end_date}"
