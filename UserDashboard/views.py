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
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import ensure_csrf_cookie
import re


# TODO: get the related stores of the user
# open => to get the cart
# all => to get the history

# 1) separate
# 2) DRY

# 1. cart_checkout  ( user_id [/] , store_id [O] , state = 'open' ) => get all open checkouts
# 2. store_store get the stores' names only
User = get_user_model()


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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOpenCheckouts(request):
    print(request.user)
    print(request.auth)
    req_user_id = request.query_params["user_id"]
    user_open_stores = CheckOut.objects.filter(user=req_user_id, state="open")
    checkouts_serializer = OrderCheckOutSerializer(user_open_stores, many=True)
    open_stores_data = {"store_id": checkouts_serializer.data}
    return Response(checkouts_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
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


# @ensure_csrf_cookie()
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateDetails(request):
    user = User.objects.get(id=request.data["user_id"])

    # if the request contains phone number change
    if "user_phone" in request.data:

        # validate phone number
        match = re.match("^01[0125][0-9]{8}$", request.data["user_phone"])
        if match:
            user.phone = request.data["user_phone"]
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    if "user_address" in request.data:
        user.address = request.data["user_address"]

    user.save()

    return Response("Done")
