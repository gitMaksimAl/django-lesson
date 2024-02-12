from django.core.management import BaseCommand

from firstapp.models import Picture


class Command(BaseCommand):

    def handle(self, *args, **options):
        image = Picture(pk=1, image="media/item_stub.png")
        image.save()
