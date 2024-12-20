# Generated by Django 3.2.16 on 2024-12-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachersubject',
            options={'verbose_name': 'Преподаватель предмета', 'verbose_name_plural': 'Преподаватели предмета'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.SmallIntegerField(default=1, verbose_name='Опыт'),
        ),
    ]
