from datetime import datetime
from typing import Optional

from django.db import models


class Coin(models.Model):

    flip_time: datetime = models.DateTimeField(auto_now_add=True)
    side: str = models.CharField(
        choices=[("head", "head"), ("tail", "tail")],
        max_length=5
    )

    @staticmethod
    def last_flips() -> dict[str, int]:
        statistic = {"head": 0, "tail": 0}
        coins = Coin.objects.all()
        for coin in coins:
            statistic[coin.side] += 1
        return statistic

    def __repr__(self):
        return f"Coin('{self.side}')"


class Author(models.Model):

    name: str = models.CharField(max_length=12)
    surname: str = models.CharField(max_length=25)
    email: str = models.EmailField()
    biography: Optional[str] = models.TextField()
    birthday: datetime = models.DateField()

    @classmethod
    def create(cls, **kwargs) -> "Author":
        return Author(
            name=kwargs["name"],
            surname=kwargs["surname"],
            email=kwargs["email"],
            biography=kwargs["biography"],
            birthday=kwargs["birthday"]
        )

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"


class Post(models.Model):

    author: int = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=200)
    description: str = models.TextField()
    date: datetime = models.DateField(auto_now_add=True)
    category: str = models.CharField(max_length=100)
    views: int = models.IntegerField(default=0)
    is_published: bool = models.BooleanField(default=False)

    def __str__(self):
        return f"Post by {self.author}, {self.title}"
