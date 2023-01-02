import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as l_

from .utils import get_image_path


class User(AbstractUser):
    is_banned = models.BooleanField(
        default=False,
        verbose_name=l_("Is user banned")
    )

    birth_date = models.DateField(
        verbose_name=l_("Birth date")
    )

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        UserPrivacySettings.objects.get_or_create(user=self)

    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
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
        if not images.exists():
            return ""
        return images.first().image.url


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
