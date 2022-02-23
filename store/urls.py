from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('store/', views.storeApi),
    path('category/', views.storecategoryApi),
    path('prices/', views.priceApi),
    path('category/bakery/', views.bakeryApi),
    path('category/pharmacy/', views.pharmacyApi),
    path('category/market/', views.marketApi),
    path('store/<str:pk>/', views.storeSelect),
    ]