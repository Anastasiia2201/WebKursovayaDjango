from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "patronimic",
        "year",
        "group",
        "avatar",
        "role",
    )
    list_editable = UserAdmin.list_editable + (
        "patronimic",
        "year",
        "group",
        "avatar",
        "role",
    )
    search_fields = (
        "username",
    )
    filter_fields = (
        "group",
        "year",
        "role",
    )

admin.site.register(User, UserAdmin)