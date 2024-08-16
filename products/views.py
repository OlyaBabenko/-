from django.middleware.csrf import get_token
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class RestaurantView(APIView):
    @staticmethod
    def get(request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductFilterRestaurantView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "restaurant__name"

    def list(self, request, **kwargs):
        serializer = ProductsSerializer(
            Product.objects.filter(restaurant__name=kwargs.get('name')),
            many=True,
            context={'request': request}
        )
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @staticmethod
    def create_db(request):
        if request.user.is_superuser:
            Product.objects.in_db_from_csv()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

    def list(self, request, **kwargs):
        if request.user.is_authenticated:
            return Response(self.get_serializer(self.queryset.filter(recipient__user=request.user.id), many=True).data,
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                return Response(self.get_serializer(self.queryset.get(user_id=request.user.id)).data,
                                status=status.HTTP_200_OK)
            except Recipient.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Object not found"})

    # def create(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         request.data.update({'user': request.user.id})
    #     return super().create(request, *args, **kwargs)


@api_view(['GET'])
def take_token(request):
    csrf_token = get_token(request)
    return Response({'csrfToken': csrf_token})
