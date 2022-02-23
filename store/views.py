from rest_framework.response import Response
from product_list.models import Product
from .models import ProductPrice, Store, StoreCategory 
from .serializers import ProductPriceSerializer, StoreSerializer, StoreCategorySerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST','GET'])
def storeApi(request):
    if request.method=='GET':
        stores = Store.objects.all()
        stores_serializer = StoreSerializer(stores, many=True)
        return Response(stores_serializer.data)
    elif request.method == 'POST':
        stores_serializer = StoreSerializer(data = request.data)
        if  stores_serializer.is_valid():
            stores_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")

@api_view(['POST','GET'])
def storecategoryApi(request):
    if request.method == 'GET':
        stores = StoreCategory.objects.all()
        stores_serializer = StoreCategorySerializer(stores, many=True)
        return Response(stores_serializer.data)
    elif request.method == 'POST':
        stores_serializer = StoreCategorySerializer(data = request.data)
        if  stores_serializer.is_valid():
            stores_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")

@api_view(['POST','GET'])
def priceApi(request):
    if request.method == 'GET':
        prices = ProductPrice.objects.all()
        prices_serializer = ProductPriceSerializer(prices, many=True)
        return Response(prices_serializer.data)
    elif request.method == 'POST':
        prices_serializer = ProductPriceSerializer(data = request.data)
        if  prices_serializer.is_valid():
            prices_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")