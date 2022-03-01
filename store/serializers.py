from itertools import product
from unicodedata import category
from rest_framework import serializers
from product_list.serializers import CategorySerializer, ProductSerializer
from store.models import  ProductOffer, Store, StoreCategory, ProductPrice


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    category_name = StoreCategorySerializer ()
    class Meta:
        model = Store
        fields = '__all__'

class ProductPriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = ProductPrice
        fields = "__all__"

class ProductOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOffer
        fields = "__all__"