from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Store
from store.serializers import StoreSerializer

# Create your views here.
@api_view(["GET"])
def ListStore(request, city):

    store_location = Store.objects.filter(city__icontains=city)
    store_location_ser = StoreSerializer(store_location, many=True)

    return Response(store_location_ser.data)


@api_view(["GET"])
def getCities(request):
    city_list = Store.objects.values_list("city", flat=True).distinct()
    return Response(city_list)
