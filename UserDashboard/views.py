from dataclasses import fields
from django.shortcuts import render
from cart.serializers import CartSerializer, CheckOutSerializer
from product_list.models import Product
from product_list.serializers import ProductSerializer
from rest_framework import serializers
from cart.models import Cart, CheckOut
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from store.models import Store
from store.serializers import ProductPriceSerializer

from rest_framework.permissions import IsAuthenticated


# TODO: get the related stores of the user
# open => to get the cart
# all => to get the history

# 1) separate
# 2) DRY

# 1. cart_checkout  ( user_id [/] , store_id [O] , state = 'open' ) => get all open checkouts
# 2. store_store get the stores' names only


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name")


"""
Get all checkouts
order id => get all nested carts [Serializer]
cart => get all nested 'products' [SlugRelated]
"""


class OrderCartSerializer(CartSerializer):
    product = ProductPriceSerializer(read_only=True)


class OrderCheckOutSerializer(CheckOutSerializer):
    store = StoreSerializer(read_only=True)
    carts = OrderCartSerializer(many=True, read_only=True)


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(["GET"])
def getOpenCheckouts(request):
    print(request.user)
    print(request.auth)
    req_user_id = request.query_params["user_id"]
    user_open_stores = CheckOut.objects.filter(user=req_user_id, state="open")
    checkouts_serializer = OrderCheckOutSerializer(user_open_stores, many=True)
    open_stores_data = {"store_id": checkouts_serializer.data}
    return Response(checkouts_serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getAllOrders(request):
    req_user_id = request.query_params["user_id"]
    user_stores = CheckOut.objects.filter(user=req_user_id)
    checkouts_serializer = OrderCheckOutSerializer(user_stores, many=True)
    open_stores_data = {"store_id": checkouts_serializer.data}
    return Response(checkouts_serializer.data)


@api_view(["GET"])
def getOrder(request, id=None):
    req_user_id = request.query_params["user_id"]
    user_stores = CheckOut.objects.filter(user=req_user_id, id=id)
    checkouts_serializer = OrderCheckOutSerializer(user_stores, many=True)
    open_stores_data = {"store_id": checkouts_serializer.data}
    return Response(checkouts_serializer.data)
