from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
import random
import logging

from .models import Coin, Author, Post


logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "myapp/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "myapp/about.html")


def game(request: HttpRequest) -> HttpResponse:
    coin = Coin(side=random.choice(["head", "tail"]))
    coin.save()
    logger.info(coin.side)
    return HttpResponse(coin.side)


def game_statistic(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Statistic: {Coin.last_flips()}")


def game2(request: HttpRequest) -> HttpResponse:
    result = f"random: {str(random.randint(1, 6))}"
    logger.info(result)
    context = {"result": result}
    return render(request, "myapp/game.html", context=context)


def game3(request: HttpRequest) -> HttpResponse:
    result = f"random: {str(random.randint(0, 1001))}"
    logger.info(result)
    context = {"result": result}
    return render(request, "myapp/game.html", context=context)


def all_authors_names(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    context = {"authors": []}
    for author in authors:
        posts = Post.objects.filter(author=author.pk, is_published=True).all()
        context["authors"].append({"author": author, "posts": posts})
    return render(request, "myapp/authors.html", context=context)


def get_post(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=pk)
        context = {"post": post}
    except ObjectDoesNotExist:
        context = {"post": None}
    return render(request, "myapp/post.html", context=context)
