# Generated by Django 3.2.16 on 2024-12-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_schedule_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='until',
            field=models.PositiveSmallIntegerField(default=17, verbose_name='До какой недели'),
        ),
    ]