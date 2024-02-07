from django.core.management import BaseCommand
from django.utils import timezone

from firstapp.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = Client(
            name="Arseni Petrovich", email="arseni@mail.ru",
            phone_number="79077176677", address="Russia, Vologda, Akima 8, 48",
            create_at=timezone.now()
        )
        client.save()
