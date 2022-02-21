from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Store, StoreCategory 
from .serializers import StoreSerializer, StoreCategorySerializer
from rest_framework.decorators import api_view


# Create your views here.

# @api_view(['POST'])
# def storeApi(request):
#     return Response({'data':"mm"})
#     if request.method=='POST ':
#         store_data=JSONParser().parse(request)
#         stores_serializer=StoreSerializer(data=store_data)
#         if stores_serializer.is_valid():
#             stores_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='POST':
#         stores = Store.objects.all()
#         stores_serializer=StoreSerializer(stores,many=True)
#         return JsonResponse(stores_serializer.data,safe=False)

@api_view(['POST','GET'])
def categoryApi(request):
    if request.method == 'GET':
        categories = StoreCategory.objects.all()
        categories_serializer = StoreCategorySerializer(categories, many=True)
        return Response(categories_serializer.data)
    elif request.method == 'POST':
        categories_serializer = StoreCategorySerializer(data = request.data)
        if  categories_serializer.is_valid():
            categories_serializer.save()
            return Response("Added Successfully")
        else:
            return Response ("NOT Valid")