from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Group
from subjects.models import Subject
from teachers.models import Teacher
from basa_mtuci.constants import CHAR_FIELD_MAX_LENGTH


class Week(models.TextChoices):
    MONDAY = 0, _("Понедельник")
    TUESDAY = 1, _("Вторник")
    WEDNESDAY = 2, _("Среда")
    THURSDAY = 3, _("Четверг")
    FRIDAY = 4, _("Пятница")
    SATURDAY = 5, _("Суббота")
    SUNDAY = 6, _("Воскресенье")


class WeekType(models.TextChoices):
    EVEN = "even", _("Четная неделя")
    UNEVEN = "uneven", _("Нечетная неделя")


class Order(models.TextChoices):
    FIRST = "1", _("1")
    SECOND = "2", _("2")
    THIRD = "3", _("3")
    FOURTH = "4", _("4")
    FIFTH = "5", _("5")


class Schedule(models.Model):
    type = models.CharField(
        verbose_name="Тип заниятия",
        null=True,
        max_length=CHAR_FIELD_MAX_LENGTH
    )
    until_week = models.PositiveSmallIntegerField(
        verbose_name="До какой недели",
        default=17,
    )
    from_week = models.PositiveSmallIntegerField(
        verbose_name="С какой недели",
        default=1,
    )
    group = models.ForeignKey(Group,
        on_delete=models.CASCADE,
        related_name='schedules'
        )
    subject = models.ForeignKey(Subject,
        null=True,
        on_delete=models.SET_NULL,
        related_name='schedules'
        )
    classroom = models.CharField(
        null=True,
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name="Аудитория",
        )
    week_type = models.CharField(
        verbose_name="Вид недели",
        choices=WeekType.choices,
        default=WeekType.UNEVEN,
        max_length=CHAR_FIELD_MAX_LENGTH
    )
    week_day = models.CharField(
        verbose_name="День недели",
        choices=Week.choices,
        default=Week.MONDAY,
        max_length=CHAR_FIELD_MAX_LENGTH
    )
    order = models.CharField(
        verbose_name="Какая пара",
        choices=Order.choices,
        default=Order.FIRST,
        max_length=CHAR_FIELD_MAX_LENGTH
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписании'
        constraints = [
            models.UniqueConstraint(
                fields=["group", "order", "week_day", "week_type"],
                name="one_per_group"
            )
        ]

    def get_day(self):
        return Schedule.Week(self.week_day)
