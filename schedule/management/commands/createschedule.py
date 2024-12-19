from django.core import management
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from schedule.views import parse_schedule

User = get_user_model()

class Command(BaseCommand):
    help = "Записать расписание из pdf-файла в БД"

    management.call_command("migrate")
    User.objects.create_superuser(
        username="admin",
        password="admin",
        email="admin@admin.com",
        first_name="Имя",
        last_name="Фамилия",
    )

    def handle(self, *args, **options):
        parse_schedule()
        self.stdout.write(self.style.SUCCESS("Данные добавлены"))
