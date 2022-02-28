from django.db import models

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
    brand = models.ForeignKey(Brand, to_field='id', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, to_field='id', on_delete=models.CASCADE)
    image = models.CharField(max_length=2550, default="", null=True)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.brand}- {self.category}"
