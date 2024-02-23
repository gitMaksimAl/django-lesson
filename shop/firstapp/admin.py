from django.contrib import admin, messages
from django.http import HttpRequest
from django.db import models

from .models import Item, Client, Picture, Order


@admin.action(description="Zeroing of items")
def update_prices(
        model_admin: admin.ModelAdmin,
        request: HttpRequest,
        queryset: models.query.QuerySet
) -> None:
    queryset.update(count=0)
    messages.info(request, "Quantity update!")


@admin.action(description="Average price of items")
def get_avg_price(
        model_admin: admin.ModelAdmin,
        request: HttpRequest,
        queryset: models.query.QuerySet
) -> None:
    mean = queryset.aggregate(models.Avg("price", default=0))
    messages.info(request, f"Average price: {round(mean['price__avg'], 2)}₽")


@admin.action(description="Check contact phone")
def is_not_have_phone(
        model_admin: admin.ModelAdmin,
        request: HttpRequest,
        queryset: models.query.QuerySet
) -> None:
    clients = queryset.filter(phone_number=None).all()
    messages.info(
        request,
        f"Clients not have phone: {chr(10).join(client.name for client in clients)}"
    )


@admin.register(Item)
class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["summary", "count", "price"]
            },
        ),
        (
            "Detail",
            {
                "classes": ["collapse"],
                "fields": ["image", "description"]
            },
        ),
    ]
    actions = [get_avg_price, update_prices]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [("name", "email")]
            },
        ),
        (
            "info",
            {
                "classes": ["collapse"],
                "fields": ["phone_number", "address", "create_at"]
            },
        ),
    ]
    actions = [is_not_have_phone]
    ordering = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [("client", "created_at")]
            },
        ),
        (
            "Detail",
            {
                "classes": ["collapse"],
                "fields": ["item"]
            },
        ),
    ]
    ordering = ("created_at",)


admin.site.register(Picture)
