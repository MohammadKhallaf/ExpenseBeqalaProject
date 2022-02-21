from django.contrib.auth.models import User
from rest_framework import serializers
from cart.models import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        # ('productID','quantity','price','orderID_id')
        fields =  '__all__'

class CheckOutSerializer(serializers.ModelSerializer):
    # carts=CartSerializer(many=True)
   
    class Meta:
        model = CheckOut
        # ('id','userID_id','storeID','orderDate')
        fields = '__all__'
    
