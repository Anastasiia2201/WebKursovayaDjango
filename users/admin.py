from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings


from .models import User


class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "patronimic",
        "registered",
        "year",
        "group",
        "avatar",
        "role",
    )
    actions = ('register',)
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
        "registered",
    )

    def register(self, request, queryset):
        for user in queryset:
            if not user.registered:
                user.registered = True
                user.save()
            confirmation_code = default_token_generator.make_token(user)
            send_mail(
                subject='Ваш код подтверждения',
                message=f'Ваш код подтверждения {str(confirmation_code)}\n Ссылка: {reverse("users:token")}',
                recipient_list=[user.email],
                from_email=settings.DEFAULT_FROM_EMAIL,
                fail_silently=False,
            )
    register.short_description = "Одобрить регистрацию (отправить код на email)"




admin.site.register(User, UserAdmin)