from django.db import models

from basa_mtuci.constants import CHAR_FIELD_MAX_LENGTH


class Subject(models.Model):
    name = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Название')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        constraints = [
            models.UniqueConstraint(
                fields=["name"], name="unique_subject_name"
            )
        ]
