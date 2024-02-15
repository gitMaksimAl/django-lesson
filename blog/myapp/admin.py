from django.contrib import admin, messages
from django.http import HttpRequest
from django.db.models import query

from .models import Coin, Author, Post


@admin.action(description="Count authors")
def authors_count(
        model_admin: admin.ModelAdmin,
        request: HttpRequest,
        queryset: query.QuerySet
) -> None:
    messages.info(request, f"Count: {queryset.count()}")


@admin.action(description="Posts themes")
def get_themes(
        model_admin: admin.ModelAdmin,
        request: HttpRequest,
        queryset: query.QuerySet
) -> None:
    themes = Post.objects.filter(author_id__in=queryset.values('pk').all()).values('category').all()
    messages.info(
        request,
        f"Themes: "
        f"{''.join(theme['category'] for theme in themes)}"
    )


class AuthorAdmin(admin.ModelAdmin):

    fieldsets: list = [
        (
            "author",
            {
                "classes": ["wide"],
                "fields": [("name", "surname")]
            },
        ),
        (
            "info",
            {
                "classes": ["collapse"],
                "fields": ["biography", "email"]
            },
        ),
    ]
    search_fields = ["name"]
    actions = [authors_count, get_themes]


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
