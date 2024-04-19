from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import UserProfile
from .serializers import UserSerializer
from .permissions import CustomUserPermission


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [CustomUserPermission]

    def perform_create(self, serializer):
        with transaction.atomic():
            user = serializer.save()
            UserProfile.objects.create(user=user)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().list(request, *args, **kwargs)
        serializer = self.get_serializer(request.user)
        return Response({"data": serializer.data})
