from django.urls import path
from .views import *


urlpatterns = [
    path('restaurant/', RestaurantView.as_view()),
    path('product/', ProductCreateView.as_view()),
    path('order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve'}), name='order-detail'),
    path('token/', take_token)
]