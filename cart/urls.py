from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', views.ListAllCheckouts, name="List all checkouts"), #list all checkouts with their order items
    path('list/<str:pk>/', views.viewCheckout, name="View checkout"),  #list specific checkout with its order item
    # path('create/checkout/', views.createCheckout, name="Create checkout"), #create an empty checkout 
    path('create/cart/', views.addItemInCart, name="add item to the cart"), #add order item in a specific checkout
    path('update/checkout/', views.updateCheckoutState, name="Update checkout state"),   # update checkout details
    path('update/cart/', views.updateCart, name="Update cart"),   # update cart details
    path('delete/cart/', views.deleteCart, name="delete cart"),   # delete cart details
    path('delete/checkout/<str:pk>/', views.deleteCheckout, name="delete checkout"),   # delete checkout 
    
]