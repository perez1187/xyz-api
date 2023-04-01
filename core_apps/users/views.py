from rest_framework import generics,permissions
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()