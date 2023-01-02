from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.html import format_html

from user.models import User, UserPrivacySettings, UserProfileImage


class UserAdmin(BaseUserAdmin):

    class UserProfileImagesInline(admin.StackedInline):
        model = UserProfileImage
        extra = 1

    list_display = BaseUserAdmin.list_display + ("age", "token", "avatar")
    inlines = (
        UserProfileImagesInline,
    )

    def has_add_permission(self, request):
        return False

    def token(self, obj):
        # TODO: Dev field, remove on release
        return obj.auth_token.key

    def avatar(self, obj):
        return format_html(f"<a href={obj.avatar}>{obj.avatar}</a>")


class UserPrivacySettingsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_allow_to_receive_messages",
        "is_visible_by_other",
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserPrivacySettings, UserPrivacySettingsAdmin)
