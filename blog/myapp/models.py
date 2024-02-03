from django.db import models
from datetime import datetime


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
    biography: str = models.TextField()
    birthday = models.DateField()

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

