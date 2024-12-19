from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

AVATAR_DIR = 'img/users/avatars/'
CHECK_DIR = 'img/users/check/'
CHAR_FIELD_MAX_LENGTH = 256


class Group(models.Model):
    name = models.CharField(
    max_length=CHAR_FIELD_MAX_LENGTH,
    verbose_name='Группа')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ("id",)
        constraints = [
            models.UniqueConstraint(
                fields=["name"], name="unique_group_name"
            )
        ]

    def __str__(self):
        return self.name

class Roles(models.TextChoices):
    USER = "user", _("Студент")
    ADMIN = "admin", _("Администратор")


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=AVATAR_DIR, default="img/teachers/no_content.jpg", verbose_name="Аватар", blank=True
    )
    role = models.CharField(
        verbose_name="Роль",
        choices=Roles.choices,
        default=Roles.USER,
        max_length=CHAR_FIELD_MAX_LENGTH
    )
    photo_check = models.ImageField(
        upload_to=CHECK_DIR, verbose_name="Фото для проверки", null=True, blank=False
    )
    patronimic = models.CharField(
        verbose_name="Отчество",
        max_length=CHAR_FIELD_MAX_LENGTH,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Курс",
        default=1
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=True,
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name="Почта",
    )
    registered = models.BooleanField(
        default=False,
        verbose_name="Зарегистрирован",
    )
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, related_name="users", verbose_name="Группа",)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == Roles.ADMIN or self.is_superuser
