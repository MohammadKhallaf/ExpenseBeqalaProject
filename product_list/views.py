from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Brand, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer, BrandSerializer

# Create your views here.

@api_view(['POST','GET'])
def productApi(request):
    if request.method=='GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
    elif request.method == 'POST':
        products_serializer = ProductSerializer(data = request.data)
        if  products_serializer.is_valid():
            products_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")



@api_view(['POST','GET'])
def categoryApi(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data)
    elif request.method == 'POST':
        categories_serializer = CategorySerializer(data = request.data)
        if  categories_serializer.is_valid():
            categories_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")


@api_view(['POST','GET'])
def brandApi(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        brands_serializer = BrandSerializer(brands, many=True)
        return Response(brands_serializer.data)
    elif request.method == 'POST':
        brands_serializer = BrandSerializer(data = request.data)
        if  brands_serializer.is_valid():
            brands_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")