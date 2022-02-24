from django.urls import include, path
from rest_framework import routers
from . import views
from location.views import ListStore
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('store/', views.storeApi),
    path('category/', views.storecategoryApi),
    path('prices/', views.priceApi),
<<<<<<< HEAD
   
=======
    path('category/bakery/', views.bakeryApi),
    path('category/pharmacy/', views.pharmacyApi),
    path('category/market/', views.marketApi),
    path('store/<str:pk>/', views.storeSelect),
>>>>>>> eb563f90d3206b7085784afbc446c7b3a03e68ae
    ]