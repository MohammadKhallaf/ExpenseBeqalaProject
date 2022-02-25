from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('stores/<str:city>/', views.ListStore, name="List Store based on location"),
    ]