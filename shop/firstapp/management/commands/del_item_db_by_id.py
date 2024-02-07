from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Item


class Command(BaseCommand):
    """
    Command remove item(by id) from database
    """

    def add_arguments(self, parser):
        parser.add_argument("item", type=int, help="Item id")

    def handle(self, *args, **options) -> None:
        try:
            item = Item.objects.get(pk=options["item"])
            item.delete()
        except ObjectDoesNotExist:
            self.stdout.write("Not have this item in db")
