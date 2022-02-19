from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', views.ListAllCheckouts, name="List All Checkouts"),
    path('list/<str:pk>/', views.viewCheckout, name="view checkout"),
]