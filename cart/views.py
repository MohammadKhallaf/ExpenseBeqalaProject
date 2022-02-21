from cmath import e
from itertools import product
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from uritemplate import partial
from cart.serializers import CheckOutSerializer, CartSerializer
from store.serializers import *
from cart.models import CheckOut, Cart
from store.models import ProductPrice
from rest_framework import status
import datetime


# view all checkouts and its order details
@api_view(["GET"])
def ListAllCheckouts(request):
    checkout = CheckOut.objects.all()
    Checkout = CheckOutSerializer(checkout, many=True)
    api_return = {"Checkout": []}
    for order in Checkout.data:
        orderDetails = {"order detail": [], "cart": [], "total": []}
        orderDetails["order detail"].append(order)
        cart = Cart.objects.filter(order_id=order["id"])
        CartSer = CartSerializer(cart, many=True)
        total = 0

        for item in CartSer.data:
            print(item)
            price = ProductPrice.objects.get(store_id=order["store_id"], product_id=item["id"])
            print(price)
            # orderDetails["cart"].append(item)
            # total += item["price"] * item["quantity"]
        orderDetails["total"].append(total)
        api_return["Checkout"].append(orderDetails)
    return Response(api_return)


# specific checkouts and its order details
@api_view(["GET"])
def viewCheckout(request, pk):
    checkout = CheckOut.objects.get(id=pk)
    Checkout = CheckOutSerializer(checkout, many=False)
    api_return = {"Checkout": []}
    orderDetails = {"order detail": [], "cart": [], "total": []}
    orderDetails["order detail"].append(Checkout.data)
    cart = Cart.objects.filter(order_id=pk)
    CartSer = CartSerializer(cart, many=True)
    total = 0
    for item in CartSer.data:
        orderDetails["cart"].append(item)
        total += item["price"] * item["quantity"]
    orderDetails["total"].append(total)
    api_return["Checkout"].append(orderDetails)

    return Response(api_return)


""" 
    - create an empty checkout in the first to add the products
        - create the product and add it to the cart 
    - add products to the existed checkout  
        - add product to the checkout if the product not existed
        - update the quatity of the product if it's existed in the cart
    
"""


@api_view(["POST"])
def addItemInCart(request):
    # check if the checkout is exist
    data = request.data
    # checkout => open , current     user , in the current      store => order id
    checkout_data = {
        "user": data["user_id"],  # edit with the current user
        "store": data["store_id"],  # sent with request
        "orderDate": datetime.datetime.now(),
    }
    checkout, created = CheckOut.objects.get_or_create(
        user_id=checkout_data["user"], store=checkout_data["store"], state="open"
    )
    # if the checkout is created we add the date with the current time stamp
    if created:
        checkout.orderDate = datetime.datetime.now()
        checkout.save()
    ## if the product exist we add its quatity to the old quatity if not we create a new one
    quantity = data["quantity"]
    try:
        oldCarts = Cart.objects.get(order_id=checkout.id, product=data["product"])
        quantity += oldCarts.quantity
        oldCarts.quantity = quantity
        oldCarts.save()
        CartSer = CartSerializer(oldCarts, many=False)
    except:
        cart_data = {
            "order": checkout.id,  # this checkout(open checkout) should be unique for (current user, currentstore)
            "product": data["product"],
            "quantity": quantity,
            "price": data["price"],
        }
        CartSer = CartSerializer(data=cart_data)
        if CartSer.is_valid():
            CartSer.save()
    return Response(CartSer.data)


# update a the checkout state only
# status code is REQUIRED as return
@api_view(["PUT"])
def updateCheckoutState(request):
    data = request.data
    state = {"state": data["state"]}
    checkout_data = {
        "user": data["user_id"],  # edit with the current user
        "store": data["store_id"],  # sent with request
        "orderDate": datetime.datetime.now(),
    }
    checkout = CheckOut.objects.filter(
        user_id=checkout_data["user"], store=checkout_data["store"], state="open"
    ).first()

    if not checkout:
        return Response(status=status.HTTP_404_NOT_FOUND)

    Checkout = CheckOutSerializer(instance=checkout, data=state, partial=True)
    if Checkout.is_valid():
        Checkout.save()
    return Response(Checkout.data)


# update the item quatity
@api_view(["PUT"])
def updateCart(request):
    data = request.data
    newQuantity = {"quantity": data["quantity"]}

    checkout_data = {
        "user": data["user_id"],  # edit with the current user
        "store": data["store_id"],  # sent with request
        "orderDate": datetime.datetime.now(),
    }
    checkout = CheckOut.objects.filter(
        user_id=checkout_data["user"], store=checkout_data["store"], state="open"
    ).first()
    if not checkout:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart = Cart.objects.get(order_id=checkout.id, product=data["product"])
    if newQuantity["quantity"] < 1:
        cart.delete()
        return Response("Order item succsesfully delete!")
    else:
        cartSer = CartSerializer(instance=cart, data=newQuantity, partial=True)
        if cartSer.is_valid():
            cartSer.save()
        return Response(cartSer.data)


# delete order item from checkout cart
@api_view(["DELETE"])
def deleteCart(request):
    data = request.data
    checkout_data = {
        "user": data["user_id"],  # edit with the current user
        "store": data["store_id"],  # sent with request
    }
    checkout = CheckOut.objects.filter(
        user_id=checkout_data["user"], store=checkout_data["store"], state="open"
    ).first()
    if not checkout:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart = Cart.objects.get(order_id=checkout.id, product=data["product"])
    cart.delete()
    return Response("Order item succsesfully delete!")


# delete checkout
@api_view(["DELETE"])
def deleteCheckout(request, pk):
    checkout = CheckOut.objects.get(id=pk)
    checkout.delete()

    return Response("Checkout succsesfully delete!")
