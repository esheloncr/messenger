from rest_framework import status
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
    UserSelfSerializer,
    UserEditSerializer
)
from .utils import is_authenticated


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


class UserSelfDetailView(GenericAPIView):
    serializer_class = UserSelfSerializer
    authentication_classes = [TokenAuthentication]

    @is_authenticated
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data)


class UserChangeView(GenericAPIView):
    serializer_class = UserEditSerializer
    authentication_classes = [TokenAuthentication]

    @is_authenticated
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = self.serializer_class(data=data, instance=user, context={
            "request": request
        })
        if serializer.is_valid():
            serializer.save()
            resized_avatar = user.get_avatar_resized()
            return Response(
                {"status": "success", "new_avatar": resized_avatar}
            )
        return Response(
            {"status": "failed", "detail": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
