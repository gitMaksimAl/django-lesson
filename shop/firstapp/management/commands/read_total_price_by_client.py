from django.core.management import BaseCommand

from firstapp.models import Client, Order


class Command(BaseCommand):
    """
    Command print out total price of clients orders
    """

    def add_arguments(self, parser):
        parser.add_argument("client", type=int, help="Client ID")

    def handle(self, *args, **options) -> None:
        client = Client.objects.first()
        self.stdout.write(f"Client: {client}, "
                          f"total price: {Order.price(client.pk)}₽")