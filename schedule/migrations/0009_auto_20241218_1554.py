# Generated by Django 3.2.16 on 2024-12-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_schedule_until'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='until',
            new_name='until_week',
        ),
        migrations.AddField(
            model_name='schedule',
            name='from_week',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='С какой недели'),
        ),
    ]
