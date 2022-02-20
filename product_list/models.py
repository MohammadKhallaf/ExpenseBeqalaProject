from django.db import models

import store.models 

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name   

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand,to_field='id', on_delete = models.CASCADE) 
    category = models.ForeignKey(Category, to_field='id', on_delete = models.CASCADE) 
    # image = models.ImageField()
    
    def __str__(self):
        return self.name


# class ProductOffer(models.Model):
#     offer = models.FloatField()
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return self.offer            

