# Generated by Django 3.2.16 on 2024-12-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teachersubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/teachers', verbose_name='Фото'),
        ),
    ]