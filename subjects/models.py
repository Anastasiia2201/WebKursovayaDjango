from django.db import models

from basa_mtuci.constants import CHAR_FIELD_MAX_LENGTH


class Subject(models.Model):
    name = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Название')

    type = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Тип сдачи',
        default='зачет')

    course_work = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Курсовая работа',
        default='нет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ("name",)
        constraints = [
            models.UniqueConstraint(
                fields=["name"], name="unique_subject_name"
            )
        ]

    def __str__(self):
        return self.name
