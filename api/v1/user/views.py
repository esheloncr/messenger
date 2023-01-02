from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from user.models import User

from .serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
