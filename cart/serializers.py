from django.contrib.auth.models import User
from rest_framework import serializers
from cart.models import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['productID','quantity','price']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'
