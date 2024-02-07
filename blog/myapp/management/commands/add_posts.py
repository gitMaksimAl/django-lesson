from random import choice, randint
from django.core.management import BaseCommand

from myapp.models import Author, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = Author.objects.all()
        for author in authors:
            for i in range(1, 11):
                post = Post(
                    author=author,
                    title=f"Post by {author.fullname} N{i}",
                    description="Text" * i,
                    category=choice(["doc", "hist", "polit", "other"]),
                    views=randint(0, i),
                    is_published=choice([True, False]),
                )
                post.save()
