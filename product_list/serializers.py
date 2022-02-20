from rest_framework import serializers

from .models import Brand, Product,Category, ProductPrice

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "brand",
            "category ",
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model =Brand
        fields = (
            "id",
            "name",
            
        )
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = (
            "id",
            "store_id",
            "product_id",
            "price",
            "offer ",
        )

# class ProductOfferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductOffer
#         fields = (
#             "id",
#             "offer",
#             "start_date",
#             "end_date",
#         )
