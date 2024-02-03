from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import random
import logging

from .models import Coin, Author


logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello mister Anderson!")


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
    return HttpResponse(result)


def game3(request: HttpRequest) -> HttpResponse:
    result = f"random: {str(random.randint(0, 1001))}"
    logger.info(result)
    return HttpResponse(result)


def all_authors_names(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    return HttpResponse("<br />".join(author.fullname for author in authors))
