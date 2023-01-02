from django.contrib.auth import authenticate
from django.utils.translation import gettext as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from user.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "age"
        )


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "full_name",
            "age"
        )

    def get_full_name(self, obj):
        return obj.get_full_name()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "password",
            "password2",
            "token"
        )

    def get_token(self, obj):
        token_obj, _ = Token.objects.get_or_create(user=obj)
        return token_obj.key

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if not password == password2:
            raise serializers.ValidationError(
                _("Passwords did not match")
            )
        attrs.pop("password2")
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = super(UserCreateSerializer, self).create(validated_data)
        instance.set_password(password)
        instance.save(update_fields=["password"])
        return instance


class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationSerializer, self).__init__(*args, **kwargs)
        self.token = None

    def validate(self, attrs):
        request = self.context.get("request")
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(request, username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                _("Incorrect username or password")
            )

        self.token = user.token

        return attrs
