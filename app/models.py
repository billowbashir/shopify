from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Shop(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=90)
    brand=models.CharField(max_length=90)
    description=models.CharField(max_length=900)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)
