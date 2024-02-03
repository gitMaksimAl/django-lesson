from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


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
