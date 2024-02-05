from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Item


class Command(BaseCommand):
    """
    Command remove item(by name) from database
    """

    def add_arguments(self, parser):
        parser.add_argument("item", type=str, help="Item summary")

    def handle(self, *args, **options) -> None:
        item = Item.objects.filter(summary__contains=options["item"]).first()
        if item is None:
            raise ObjectDoesNotExist("Not have this item")
        item.delete()
