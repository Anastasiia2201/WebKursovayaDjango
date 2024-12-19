from django.db import models

from basa_mtuci.constants import CHAR_FIELD_MAX_LENGTH
from subjects.models import Subject

class Teacher(models.Model):
    first_name = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Фамилия')
    patronimic = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Отчество')
    bio = models.TextField(
        verbose_name='Текст')
    image = models.ImageField('Фото', default="img/teachers/no_content.jpg", upload_to='img/teachers')
    experience = models.SmallIntegerField(default=1, verbose_name='Опыт')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ("last_name",)

    def __str__(self):
        return self.last_name


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'Преподаватель предмета'
        verbose_name_plural = 'Преподаватели предмета'

    def __str__(self):
        return str(self.id)
