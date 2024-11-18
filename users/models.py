from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

AVATAR_DIR = 'users/'
CHAR_FIELD_MAX_LENGTH = 256


class Group(models.Model):
    name = models.CharField(
    max_length=CHAR_FIELD_MAX_LENGTH,
    verbose_name='Группа')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ("id",)


class Roles(models.TextChoices):
    USER = "user", _("Студент")
    ADMIN = "admin", _("Администратор")


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=AVATAR_DIR, verbose_name="Аватар", null=True, blank=True
    )
    role = models.CharField(
        verbose_name="Роль",
        choices=Roles.choices,
        default=Roles.USER,
        max_length=CHAR_FIELD_MAX_LENGTH
    )
    patronimic = models.CharField(
        verbose_name="Отчество",
        max_length=CHAR_FIELD_MAX_LENGTH,
    )
    year = models.SmallIntegerField(
        verbose_name="Курс",
        default=1
    )
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, related_name="users")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == Roles.ADMIN or self.is_superuser
