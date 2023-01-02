from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from user.models import User, UserPrivacySettings


class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("age", "token")

    def has_add_permission(self, request):
        return False

    def token(self, obj):
        # TODO: Dev field, remove on release
        return obj.auth_token.key


class UserPrivacySettingsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_allow_to_receive_messages",
        "is_visible_by_other",
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserPrivacySettings, UserPrivacySettingsAdmin)
