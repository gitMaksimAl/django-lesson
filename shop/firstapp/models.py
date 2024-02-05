from django.db import models
from datetime import datetime


class Client(models.Model):
    name: str = models.CharField(max_length=255)
    email: str = models.EmailField()
    phone_number: str = models.CharField(max_length=50)
    address: str = models.CharField(max_length=255)
    create_at: datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.email} {self.phone_number}"


class Item(models.Model):
    summary: str = models.CharField(max_length=25)
    description: str = models.TextField()
    price: float = models.DecimalField(decimal_places=2, max_digits=7)
    count: int = models.IntegerField()
    added_at: datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.summary}: {self.price}₽"


class Order(models.Model):
    client: int = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    item: int = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    created_at: datetime = models.DateTimeField()

    @staticmethod
    def price(pk: int):
        total_price = Order.objects.filter(client=pk) \
            .select_related("item") \
            .aggregate(models.Sum("item__price"))["item__price__sum"]
        return round(total_price, 2)

    def __str__(self):
        return f"Order №{self.pk} {self.created_at}: {self.client}, {self.item}"

