from django import forms
from .models import Shop

class NewShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        exclude=['owner']
    
