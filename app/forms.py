from django import forms
from .models import Shop,Product

class NewShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        exclude=['owner']

class NewProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=['shop']
