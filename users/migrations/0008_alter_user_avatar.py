# Generated by Django 3.2.16 on 2024-12-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='img/teachers/no_content.jpg', upload_to='img/users/avatars/', verbose_name='Аватар'),
        ),
    ]
