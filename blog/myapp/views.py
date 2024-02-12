import random
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Coin, Author, Post
from .forms import Game, AuthorForm, PostForm


logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "myapp/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "myapp/about.html")


def game(request: HttpRequest) -> dict[str, str]:
    coin = Coin(side=random.choice(["head", "tail"]))
    coin.save()
    logger.info(coin.side)
    return {"result": coin.side}


def game_statistic(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Statistic: {Coin.last_flips()}")


def game2(request: HttpRequest) -> dict[str, str]:
    result = f"random: {str(random.randint(1, 6))}"
    logger.info(result)
    context = {"result": result}
    return context


def choice_game(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = Game(request.POST)
        if form.is_valid():
            context = None
            match form.data["game_name"]:
                case "coin":
                    context = game(request)
                case "cube":
                    context = game2(request)
                case "number":
                    result = f"random: {str(random.randint(1, 1001))}"
                    logger.info(result)
                    context = {"result": result}
            return render(request, "myapp/game.html", context=context)
    form = Game()
    return render(request, "myapp/game.html", {"form": form})


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


def add_author(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = Author(
                name=form.data["name"],
                surname=form.data["surname"],
                email=form.data["email"],
                biography=form.data["biography"],
                birthday=form.data["birthday"]
            )
            new_author.save()
        return render(request, "myapp/new_author.html", context={"form": form})
    form = AuthorForm()
    return render(request, "myapp/new_author.html", context={"form": form})


def add_post(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                author = Author.objects.get(pk=form.data["author"])
                new_post = Post(
                    author=author,
                    title=form.data["title"],
                    description=form.data["description"],
                    category=form.data["category"],
                    views=form.data["views"]
                )
                new_post.save()
            except ObjectDoesNotExist:
                logger.error(f"author {form.data['auhtor']} not available")
            finally:
                return render(request, "myapp/new_author.html", context={"form": form})
    form = PostForm()
    return render(request, "myapp/new_author.html", context={"form": form})
