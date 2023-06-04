from django.middleware.csrf import get_token
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class RestaurantView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        name = request.GET.get('name')
        restaurant = Restaurant.objects.get(name=name)
        dishes = Product.objects.filter(restaurant=restaurant)
        serializer = ProductsSerializer(dishes, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def take_token(request):
    csrf_token = get_token(request)
    return Response({'csrfToken': csrf_token})
