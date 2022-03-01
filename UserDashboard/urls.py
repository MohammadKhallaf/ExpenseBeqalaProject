from django.urls import path, include

from . import views

urlpatterns = [
    path('open-stores/',views.getOpenCheckouts),
    path('orders/',views.getAllOrders),
    path('orders/<str:id>',views.getOrder),
]
