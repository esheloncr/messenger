import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as l_

from sorl.thumbnail import get_thumbnail

from .utils import get_image_path


class User(AbstractUser):
    USER_AVATAR_PLACEHOLDER_PATH = 'user/static/img/user_photo_placeholder.png'
    is_banned = models.BooleanField(
        default=False,
        verbose_name=l_("Is user banned")
    )

    birth_date = models.DateField(
        verbose_name=l_("Birth date")
    )

    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['birth_date']

    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day) # noqa
        )
        return age

    @property
    def token(self):
        has_token = hasattr(self, 'auth_token')
        if has_token:
            return self.auth_token.key
        return ""

    @cached_property
    def avatar(self):
        images = self.images.filter(is_avatar=True)
        return images.first().image.url

    def unset_avatar(self):
        """
        Change current avatar to non-avatar picture.
        """
        image_obj = self.images.filter(is_avatar=True).first()
        if image_obj:
            image_obj.is_avatar = False
            image_obj.save(update_fields=["is_avatar"])

    def change_avatar(self, avatar):
        """
        Create an image object and set it as avatar.
        """
        image_data = {
            "image": avatar,
            "is_avatar": True
        }
        self.unset_avatar()
        self.images.create(**image_data)

    def get_avatar_resized(self, crop_size="150x150"):
        avatar = self.images.filter(is_avatar=True)
        avatar_obj = avatar.first().image
        image = get_thumbnail(avatar_obj, crop_size, crop='center', quality=99)
        return image.url

    def save(self, *args, **kwargs):
        if self.pk and not self.images.filter(is_avatar=True).exists():
            from django.core.files.images import ImageFile
            self.images.create(
                is_avatar=True,
                image=ImageFile(open(self.USER_AVATAR_PLACEHOLDER_PATH, 'rb'))
            )
        return super(User, self).save(*args, **kwargs)


class UserPrivacySettings(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=l_("User"),
        related_name="settings"
    )

    # Messages settings
    is_allow_to_receive_messages = models.BooleanField(
        default=True,
        verbose_name=l_("Can user receive messages")
    )

    # Profile settings
    is_visible_by_other = models.BooleanField(
        default=True,
        verbose_name=l_("User information visibility")
    )

    class Meta:
        verbose_name = l_("User privacy settings")
        verbose_name_plural = l_("User privacy settings")


class UserProfileImage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=l_("User profile images")
    )

    image = models.ImageField(upload_to=get_image_path)
    is_avatar = models.BooleanField(
        default=False,
        verbose_name=l_("Main image of profile")
    )

    def __str__(self):
        return f"{self.user.username} image"
