from django import forms

from .models import Item, Picture


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["summary", "description", "price", "count", "image"]


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ["image"]
