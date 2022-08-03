from django import forms
from .models import Cart


class CartViewForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)
