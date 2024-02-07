from django.core.management import BaseCommand
from django.utils import timezone

from firstapp.models import Item


class Command(BaseCommand):
    """
    Command add three difference items to database
    """

    def handle(self, *args, **options) -> None:
        item = Item(
            summary="Samsung S23", description="Nice phone",
            price=999.99, count=50, added_at=timezone.now()
        )
        item2 = Item(
            summary="Lenovo Thinkpad", description="Nice laptop",
            price=999.99, count=10, added_at=timezone.now()
        )
        item3 = Item(
            summary="Kawasaki H2R", description="Nice bike",
            price=999.99, count=10, added_at=timezone.now()
        )
        item.save()
        item2.save()
        item3.save()
