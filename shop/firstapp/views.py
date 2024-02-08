from decimal import Decimal

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist

from .models import Order, Item, Client


def main_page(request: HttpRequest):
    content = """
    <center><h1>GB Shop</h1></center>
    <p>This is a main page of our magazine</p>
    """
    return HttpResponse(content=content.encode("utf-8"))


def about_page(request: HttpRequest):
    content = """
    <center><h1>About us</h1></center>
    <ul>
        <li>our suppliers</li>
        <li>our customers</li>
        <li>our sponsors</li>
    </ul>
    """
    return HttpResponse(content=content.encode("utf-8"))


def all_orders(request: HttpRequest) -> HttpResponse:
    orders = Order.objects.all().order_by("client")
    ords = [
        f"<li>{order}</li>"
        for order in orders
    ]
    content = f"<center><h1>Orders</h1></center><ul>{''.join(ords)}</ul>"
    return HttpResponse(content=content)


def all_items(request: HttpRequest) -> HttpResponse:
    items = Item.objects.all()
    all_item = [
        f"<li>{item}</li>"
        for item in items
    ]
    content = f"<center><h1>Items</h1></center><ul>{''.join(all_item)}</ul>"
    return HttpResponse(content=content)


def get_item(request: HttpRequest, item_pk: int) -> HttpResponse:
    try:
        item = Item.objects.get(pk=item_pk)
        context = {"item": item}
    except ObjectDoesNotExist:
        context = {"item": None}
    return render(request, "firstapp/item.html", context=context)


def client_orders(request: HttpRequest, client_pk: int) -> HttpResponse:
    my_orders = Order.objects\
        .filter(client_id=client_pk)\
        .select_related("item")\
        .distinct()
    today = now()
    orders = {"orders": {}}
    for order in my_orders:
        if (today - order.created_at).days < 7:
            orders["orders"].setdefault("lt_week", {
                "title": "On last week",
                "items": [],
                "total": Decimal(0)
            })
            orders["orders"]["lt_week"]["items"].append(order)
            orders["orders"]["lt_week"]["total"] += order.item.price
        elif (today - order.created_at).month == 0:
            orders["orders"].setdefault("lt_month", {
                "title": "In last month",
                "items": [],
                "total": Decimal(0)
            })
            orders["orders"]["lt_month"]["items"].append(order)
            orders["orders"]["lt_week"]["total"] += order.item.price
        elif (today - order.created_at).year == 0:
            orders["orders"].setdefault("lt_year", {
                "title": "In last year",
                "items": [],
                "total": Decimal(0)
            })
            orders["orders"]["lt_year"]["items"].append(order)
            orders["orders"]["lt_week"]["total"] += order.item.price
    return render(request, "firstapp/order.html", context=orders)
