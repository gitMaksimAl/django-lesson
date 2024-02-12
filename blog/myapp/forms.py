from datetime import datetime

from django import forms

from .models import Author, Post


class Game(forms.Form):
    game_name: str = forms.ChoiceField(choices=[
        ("coin", "Coin"),
        ("cube", "Cube"),
        ("number", "Number")
    ])
    attempts = forms.IntegerField(min_value=1, max_value=12)
#
#
# class AuthorForm(forms.Form):
#     name: str = forms.CharField(max_length=12)
#     surname: str = forms.CharField(max_length=25)
#     email: str = forms.CharField(widget=forms.EmailInput)
#     biography: str = forms.CharField(widget=forms.Textarea)
#     birthday: datetime = forms.DateField(input_formats=["%Y-%m-%d"])


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ["name", "surname", "email", "biography", "birthday"]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["author", "title", "description", "category", "views"]
