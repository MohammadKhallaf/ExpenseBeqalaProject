# from unicodedata import category
from rest_framework import serializers
from store.models import Store, StoreCategory


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = (
            "id",
            "name", 
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        stores = StoreCategorySerializer ( many = True)
        fields = '__all__'
        

