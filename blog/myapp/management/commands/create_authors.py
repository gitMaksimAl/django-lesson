from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand

from myapp.models import Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(1, 11):
            author = Author(
                name=f"Name{i}",
                surname=f"Surname{i}",
                email=f"name{i}@mail.ru",
                biography=f"Biography of Name{i} Surname{i}",
                birthday=timezone.now() - timedelta(days=i*3650)
            )
            author.save()
