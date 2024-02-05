from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

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
