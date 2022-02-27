from django.contrib.auth import get_user_model
from accounts.models import *
from store.models import *
from django.contrib.auth import get_user_model

from accounts.models import *

# Create your models here.
User = get_user_model()


class CheckOut(models.Model):
    # orderDate updated when done checkout
    STATE_CHOICES = (
        ('open', 'OPEN'),
        ('pending', 'PENDING'),
        ('done', 'DONE'),
    )
    PAYMENT_CHOICES = (
        ('none', 'NONE'),
        ('cash', 'CASH'),
        ('credit', 'CREDIT'),
        ('paypal', 'PAYPAL'),
    )
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, to_field='id', on_delete=models.CASCADE, related_name='store')
    orderDate = models.DateTimeField(null=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='open')
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')
    def __str__(self):
        return f"{self.user} - {self.store} - {self.id}"


class Cart(models.Model):
    order = models.ForeignKey(CheckOut, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(ProductPrice, to_field='id', on_delete=models.CASCADE, related_name='cartProduct')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.product} - {self.quantity}"
