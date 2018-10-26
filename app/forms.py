from django import forms
from .models import Shop,Product,Order

class NewShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        exclude=['owner']

class NewProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=['shop']
class NewOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['quantity']
