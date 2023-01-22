from django.http import Http404

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    GenericAPIView
)
from rest_framework.response import Response

from user.models import User

from .serializers import (
    UserListSerializer,
    UserDetailSerializer,
    UserCreateSerializer,
    UserAuthenticationSerializer,
    UserSelfShortSerializer
)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserAuthenticateView(GenericAPIView):
    serializer_class = UserAuthenticationSerializer
    queryset = User.objects.exclude(is_superuser=True)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            "token": serializer.token
        }
        return Response(data)


class UserSelfShortDetailView(GenericAPIView):
    serializer_class = UserSelfShortSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise Http404

        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)
