from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from firstapp.models import Order, Client, Item


class Command(BaseCommand):
    """
    Command remove all client orders(by client id)
    """

    def add_arguments(self, parser):
        parser.add_argument("client", type=int, help="Client ID")

    def handle(self, *args, **options):
        try:
            client = Client.objects.get(pk=options["client"])
            orders = Order.objects.filter(client).all()
            for order in orders:
                order.delete()
        except ObjectDoesNotExist:
            self.stdout.write("\x1B[94;105mNot have this items in db\x1B[m")
