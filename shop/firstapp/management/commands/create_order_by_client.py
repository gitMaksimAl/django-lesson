from django.core.management import BaseCommand
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Order, Client, Item


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("item", type=int, help="Item ID")
        parser.add_argument("client", type=int, help="Client ID")

    def handle(self, *args, **options):
        try:
            db_client = Client.objects.get(pk=options["client"])
            db_item = Item.objects.get(pk=options["item"])
            order = Order(client=db_client, item=db_item, created_at=timezone.now())
            order.save()
        except ObjectDoesNotExist:
            self.stdout.write("\x1B[94;105mNot have this items in db\x1B[m")

