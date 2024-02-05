from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Item


class Command(BaseCommand):
    """
    Command change price of the item in database
    """

    def add_arguments(self, parser):
        parser.add_argument("item", type=int, help="Item ID")
        parser.add_argument("price", type=float, help="Item price")

    def handle(self, *args, **options) -> None:
        try:
            item = Item.objects.get(pk=options["item"])
            item.price = options["price"]
            item.save()
        except ObjectDoesNotExist:
            self.stdout.write("Not have this item in database")
