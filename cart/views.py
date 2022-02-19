from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.serializers import CheckOutSerializer, CartSerializer
from cart.models import CheckOut, Cart

# view all checkouts and its order details
@api_view(['GET'])
def ListAllCheckouts(request):

    checkout = CheckOut.objects.all()
    Checkout = CheckOutSerializer(checkout, many=True)
    api_return = {
       'Checkout': []
    }
    for order in Checkout.data:
        orderDetails = {
            'order detail': [],
            'cart': [],
            'total': []
        
        }
        orderDetails['order detail'].append(order)
        cart = Cart.objects.filter(orderID=order['id'])
        CartSer = CartSerializer(cart, many=True)
        total=0
        for item in CartSer.data:
            orderDetails['cart'].append(item)
            total+=(item['price']*item['quantity'])
        orderDetails['total'].append(total)
        api_return['Checkout'].append(orderDetails)
        
    return Response(api_return)

# specific checkouts and its order details
@api_view(['GET'])
def viewCheckout(request,pk):

    checkout = CheckOut.objects.get(id=pk)
    Checkout = CheckOutSerializer(checkout, many=False)
    api_return = {
       'Checkout': []
    }
   
    orderDetails = {
        'order detail': [],
        'cart': [],
        'total': []
    
    }
    orderDetails['order detail'].append(Checkout.data)
    cart = Cart.objects.filter(orderID=pk)
    CartSer = CartSerializer(cart, many=True)
    total=0
    for item in CartSer.data:
        orderDetails['cart'].append(item)
        total+=(item['price']*item['quantity'])
    orderDetails['total'].append(total)
    api_return['Checkout'].append(orderDetails)
    
    return Response(api_return)
