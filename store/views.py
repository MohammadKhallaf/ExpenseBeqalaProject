from itertools import product
from rest_framework.response import Response
from uritemplate import partial
from product_list.models import Product
from product_list.serializers import ProductSerializer
from .models import ProductPrice, Store, StoreCategory
from .serializers import ProductPriceSerializer, StoreSerializer, StoreCategorySerializer
from rest_framework.decorators import api_view

# from rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.

@api_view(['POST', 'GET'])
def storeApi(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        stores_serializer = StoreSerializer(stores, many=True)
        return Response(stores_serializer.data)
    elif request.method == 'POST':
        stores_serializer = StoreSerializer(data=request.data)
        if stores_serializer.is_valid():
            stores_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("NOT Valid")


@api_view(['POST', 'GET'])
def storecategoryApi(request):
    if request.method == 'GET':
        stores = StoreCategory.objects.all()
        stores_serializer = StoreCategorySerializer(stores, many=True)
        return Response(stores_serializer.data)
    elif request.method == 'POST':
        stores_serializer = StoreCategorySerializer(data=request.data)
        if stores_serializer.is_valid():
            stores_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("NOT Valid")


@api_view(['POST', 'GET'])
def priceApi(request):
    if request.method == 'GET':
        prices = ProductPrice.objects.all()
        prices_serializer = ProductPriceSerializer(prices, many=True)
        return Response(prices_serializer.data)
    elif request.method == 'POST':
        prices_serializer = ProductPriceSerializer(data=request.data)
        if prices_serializer.is_valid():
            prices_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("NOT Valid")


@api_view(['GET'])
def bakeryApi(request):
    request.method == 'GET'
    bakery = Store.objects.filter(category_name_id=1)
    serializer = StoreSerializer(bakery, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pharmacyApi(request):
    request.method == 'GET'
    pharmacy = Store.objects.filter(category_name_id=2)
    serializer = StoreSerializer(pharmacy, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def marketApi(request):
    request.method == 'GET'
    market = Store.objects.filter(category_name_id=3)
    serializer = StoreSerializer(market, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def storeSelect(request, pk):
    productprice = ProductPrice.objects.filter(store_id=pk)
    productprice_serializer = ProductPriceSerializer(productprice, many=True)
    return Response(productprice_serializer.data)


@api_view(['GET'])
def alexApi(request):
    request.method == 'GET'
    market = Store.objects.filter(city="Alexandria")
    serializer = StoreSerializer(market, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cairoApi(request):
    request.method == 'GET'
    market = Store.objects.filter(city="Cairo")
    serializer = StoreSerializer(market, many=True)
    return Response(serializer.data)


"""
1. choose the store
2. save in product price list 
3. 
|> user -> store
|> user & store & product -> ++ product price
"""


@api_view(["GET", "POST", "PUT", "DELETE"])
def productOfStore(request):
    if request.method == "GET":
        data = request.query_params
    else:
        data = request.data
    print(data)
    user_id = data['owner_id']
    user_store = Store.objects.filter(user_account_id=user_id).first()

    if request.method == "POST":
        product_id = data['product_id']
        product_price_item = ProductPrice.objects.get_or_create(
            store_id=user_store.id, product_id=product_id)
    elif request.method == 'PUT':
        product_price_id = request.data['product_price_id']
        product_price_value = request.data['product_price_value']
        product_price = ProductPrice.objects.get(id=product_price_id)
        product_price_serializer = ProductPriceSerializer(
            product_price, data={'price': product_price_value}, partial=True)
        if product_price_serializer.is_valid():
            product_price_serializer.save()
        else:
            return Response("NOT Valid")
    elif request.method == "DELETE":
        product_price_id = request.data['product_price_id']
        product_price = ProductPrice.objects.get(id=product_price_id)
        product_price.delete()

    all_products = ProductPrice.objects.filter(store_id=user_store.id)
    storeProduct_serializer = ProductPriceSerializer(all_products, many=True)
    return Response(storeProduct_serializer.data)
