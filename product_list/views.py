from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST', 'DELETE'])
def productApi(request):

    print('X'*3)

    print(request.method)
    print('..............................................................')
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
    elif request.method == 'POST':
        products_serializer = ProductSerializer(data=request.data)
        print(products_serializer)
        if products_serializer.is_valid():

            products_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("product is not Valid")

    elif request.method == 'DELETE':
        # delete all
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def individualProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        product_selializer = ProductSerializer(product, many=False)
        return Response(product_selializer.data)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product_selializer = ProductSerializer(product, product_data)
        if product_selializer.is_valid():
            product_selializer.save()
            return JsonResponse(product_selializer.data)
        return JsonResponse(product_selializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT', 'DELETE'])
# def productApi(request):
#     if request.method == 'DELETE':
#         products = Product.objects.get('name')
#         products_serializer = ProductSerializer(products)
#         return Response(products_serializer.data)
#     elif request.method == 'POST':
#         products_serializer = ProductSerializer(data=request.data)
#         if products_serializer.is_valid():
#             products_serializer.save()
#             return Response("Added Successfully")
#         else:
#             return Response("NOT Valid")


@api_view(['POST', 'GET'])
def categoryApi(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data)
    elif request.method == 'POST':
        categories_serializer = CategorySerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("NOT Valid")


@api_view(['POST', 'GET'])
def brandApi(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        brands_serializer = BrandSerializer(brands, many=True)
        return Response(brands_serializer.data)
    elif request.method == 'POST':
        brands_serializer = BrandSerializer(data=request.data)
        if brands_serializer.is_valid():
            brands_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("NOT Valid")
