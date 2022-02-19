from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product_list.serializers import ProductSerializer
from product_list.models import Product


class TesView(APIView):
    def get(self, request, *args, **kwargs):
        data =[{"id":1,"name":"Momiji Oroshi Chili Sauce","description":"Caville","price":"$0.86","image":"http://dummyimage.com/161x100.png/dddddd/000000"},
{"id":2,"name":"Veal - Provimi Inside","description":"Humfrey","price":"$7.45","image":"http://dummyimage.com/236x100.png/dddddd/000000"},
{"id":3,"name":"Bag - Bread, White, Plain","description":"Cookney","price":"$6.03","image":"http://dummyimage.com/130x100.png/dddddd/000000"},
{"id":4,"name":"Bread - Kimel Stick Poly","description":"Barends","price":"$9.07","image":"http://dummyimage.com/121x100.png/ff4444/ffffff"},
{"id":5,"name":"Initation Crab Meat","description":"Cohr","price":"$0.24","image":"http://dummyimage.com/135x100.png/5fa2dd/ffffff"},
{"id":6,"name":"Potatoes - Instant, Mashed","description":"Harrowell","price":"$10.00","image":"http://dummyimage.com/198x100.png/cc0000/ffffff"},
{"id":7,"name":"Cheese - Augre Des Champs","description":"Rains","price":"$8.75","image":"http://dummyimage.com/170x100.png/ff4444/ffffff"},
{"id":8,"name":"Eel Fresh","description":"Ceccoli","price":"$3.15","image":"http://dummyimage.com/227x100.png/dddddd/000000"},
{"id":9,"name":"Flower - Carnations","description":"Georghiou","price":"$2.74","image":"http://dummyimage.com/215x100.png/dddddd/000000"},
{"id":10,"name":"Lamb Shoulder Boneless Nz","description":"Cammoile","price":"$1.36","image":"http://dummyimage.com/123x100.png/cc0000/ffffff"},
{"id":11,"name":"Galliano","description":"Matuszynski","price":"$2.58","image":"http://dummyimage.com/136x100.png/dddddd/000000"},
{"id":12,"name":"Aspic - Amber","description":"Beinke","price":"$7.86","image":"http://dummyimage.com/184x100.png/dddddd/000000"},
{"id":13,"name":"Snapple - Iced Tea Peach","description":"Matt","price":"$5.59","image":"http://dummyimage.com/177x100.png/5fa2dd/ffffff"},
{"id":14,"name":"Scallops - Live In Shell","description":"Bluett","price":"$3.01","image":"http://dummyimage.com/202x100.png/ff4444/ffffff"},
{"id":15,"name":"Alize Gold Passion","description":"Baiden","price":"$7.30","image":"http://dummyimage.com/187x100.png/dddddd/000000"},
{"id":16,"name":"Coffee - Almond Amaretto","description":"Gabbitas","price":"$2.12","image":"http://dummyimage.com/129x100.png/dddddd/000000"},
{"id":17,"name":"Wine - Baron De Rothschild","description":"Darkin","price":"$9.32","image":"http://dummyimage.com/208x100.png/5fa2dd/ffffff"},
{"id":18,"name":"Beer - Camerons Auburn","description":"Tregear","price":"$7.74","image":"http://dummyimage.com/130x100.png/cc0000/ffffff"},
{"id":19,"name":"Steampan - Half Size Shallow","description":"Westraw","price":"$6.94","image":"http://dummyimage.com/205x100.png/5fa2dd/ffffff"},
{"id":20,"name":"The Pop Shoppe - Black Cherry","description":"Doerffer","price":"$2.79","image":"http://dummyimage.com/166x100.png/cc0000/ffffff"},
{"id":21,"name":"Soup - Campbells","description":"Crossfield","price":"$1.59","image":"http://dummyimage.com/133x100.png/cc0000/ffffff"},
{"id":22,"name":"Soap - Hand Soap","description":"Rosenthal","price":"$4.05","image":"http://dummyimage.com/121x100.png/dddddd/000000"},
{"id":23,"name":"Cheese Cloth No 100","description":"Severn","price":"$7.06","image":"http://dummyimage.com/144x100.png/ff4444/ffffff"},
{"id":24,"name":"Huck Towels White","description":"Swiggs","price":"$4.80","image":"http://dummyimage.com/103x100.png/ff4444/ffffff"},
{"id":25,"name":"Rice Paper","description":"Wateridge","price":"$2.63","image":"http://dummyimage.com/119x100.png/ff4444/ffffff"},
{"id":26,"name":"Wine - Lamancha Do Crianza","description":"Baselli","price":"$7.56","image":"http://dummyimage.com/200x100.png/cc0000/ffffff"},
{"id":27,"name":"Truffle - Peelings","description":"Peperell","price":"$6.36","image":"http://dummyimage.com/238x100.png/ff4444/ffffff"},
{"id":28,"name":"Wine - Casablanca Valley","description":"Clows","price":"$6.38","image":"http://dummyimage.com/143x100.png/cc0000/ffffff"},
{"id":29,"name":"Beef - Chuck, Boneless","description":"Kenelin","price":"$4.21","image":"http://dummyimage.com/169x100.png/cc0000/ffffff"},
{"id":30,"name":"Cut Wakame - Hanawakaba","description":"Alasdair","price":"$2.33","image":"http://dummyimage.com/117x100.png/5fa2dd/ffffff"}]
        return Response(data)
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)