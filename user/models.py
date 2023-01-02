import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as l_


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
