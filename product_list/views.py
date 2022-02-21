from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Product
from .serializers import ProductSerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        products = Product.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)