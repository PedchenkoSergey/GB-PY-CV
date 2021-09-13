from django import forms
from .models import GoodModel


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = GoodModel
        exclude = ('created_date',)

