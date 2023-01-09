from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class ResizedAvatarMixin(metaclass=serializers.SerializerMetaclass):
    avatar_resized = serializers.SerializerMethodField()
    crop_size = '100x100'

    def get_avatar_resized(self, obj):
        crop_size = self.crop_size
        avatar = obj.images.filter(is_avatar=True)
        avatar_obj = avatar.first().image
        image = get_thumbnail(avatar_obj, crop_size, crop='center', quality=99)
        return image.url
