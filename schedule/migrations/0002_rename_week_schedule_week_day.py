# Generated by Django 3.2.16 on 2024-11-19 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='week',
            new_name='week_day',
        ),
    ]