from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import random
import logging

logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello mister Anderson!")


def game(request: HttpRequest) -> HttpResponse:
    result = random.choice(["head", "tail"])
    logger.info(result)
    return HttpResponse(result)


def game2(request: HttpRequest) -> HttpResponse:
    result = f"random: {str(random.randint(1, 6))}"
    logger.info(result)
    return HttpResponse(result)


def game3(request: HttpRequest) -> HttpResponse:
    result = f"random: {str(random.randint(0, 1001))}"
    logger.info(result)
    return HttpResponse(result)
