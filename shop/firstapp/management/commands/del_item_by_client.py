from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Order, Client, Item


class Command(BaseCommand):
    """
    Command remove item(by name) from client order(by client id)
    """

    def add_arguments(self, parser):
        parser.add_argument("client", type=int, help="Client ID")
        parser.add_argument("item", type=str, help="Item summary")

    def handle(self, *args, **options) -> None:
        try:
            client = Client.objects.get(pk=options["client"])
            item = Item.objects.filter(summary__contains=options["item"]).first()
            orders = Order.objects.filter(client=client.pk, item=item.pk).all()
            for order in orders:
                order.delete()
        except ObjectDoesNotExist:
            self.stdout.write("\x1B[94;105mNot have this items in db\x1B[m")
