# Generated by Django 3.2.16 on 2024-12-18 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_auto_20241218_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('name',), 'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
