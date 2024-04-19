from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'recipient', RecipientViewSet, basename="recipient")
router.register(r'order', OrderViewSet, basename="order")
router.register(r'', ProductViewSet, basename="product")

urlpatterns = [
    path('restaurant/', RestaurantView.as_view()),
    path('product/create_db', ProductFilterRestaurantView.as_view({"get": "create_db"})),
    path('product/<str:name>/', ProductFilterRestaurantView.as_view({"get": "list"})),
    path('token/', take_token),
    path("", include(router.urls)),
]
