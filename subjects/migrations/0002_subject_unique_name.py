# Generated by Django 3.2.16 on 2024-11-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subject',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_name'),
        ),
    ]
