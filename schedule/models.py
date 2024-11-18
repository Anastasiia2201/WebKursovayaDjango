from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_LENGTH = 256

from users.models import Group


class Week(models.TextChoices):
    MONDAY = "mn", _("Понедельник")
    TUESDAY = "tu", _("Вторник")
    WEDNESDAY = "wd", _("Среда")
    THURSDAY = "th", _("Четверг")
    FRIDAY = "fr", _("Пятница")
    SATURDAY = "st", _("Суббота")
    SUNDAY = "sn", _("Воскресенье")


class WeekType(models.TextChoices):
    EVEN = "even", _("Четная неделя")
    UNEVEN = "uneven", _("Нечетная неделя")


class Order(models.TextChoices):
    FIRST = "1", _("1")
    SECOND = "2", _("2")
    THIRD = "3", _("3")
    FOURTH = "4", _("4")
    FIFTH = "5", _("5")


class Subject(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Classroom(models.Model):
    classroom = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Аудитория')

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class Schedule(models.Model):
    group = models.ForeignKey(Group,
        on_delete=models.CASCADE,
        related_name='schedules'
        )
    subject = models.ForeignKey(Subject,
        on_delete=models.CASCADE,
        related_name='schedules'
        )
    classroom = models.ForeignKey(
        Classroom,
        null=True,
        on_delete=models.SET_NULL,
        related_name='schedules'
        )
    week_type = models.CharField(
        verbose_name="Вид недели",
        choices=WeekType.choices,
        default=WeekType.UNEVEN,
        max_length=MAX_LENGTH
    )
    week = models.CharField(
        verbose_name="День недели",
        choices=Week.choices,
        default=Week.MONDAY,
        max_length=MAX_LENGTH
    )
    order = models.CharField(
        verbose_name="Какая пара",
        choices=Order.choices,
        default=Order.FIRST,
        max_length=MAX_LENGTH
    )
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписании'
