from django import forms
from .models import Merchant, ProductType

class LoginForm(forms.Form):
    userName = forms.CharField(label='Your user name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class OrderForm(forms.Form):
    PRODUCT_TYPE = (
        ('Fragile','Fragile'),
        ('Liquid','Liquid')
    )
    DELIVERY_LOCATION = (
        (0,'Inside of Dhaka'),
        (1,'Division of Dhaka'),
        (2,'Outside of Dhaka')
    )
    merchent = forms.ModelChoiceField(label='Merchant', queryset=Merchant.objects.all())
    parcelType= forms.ModelChoiceField(label='Select Parcel Product Type', queryset=ProductType.objects.all())
    weight = forms.FloatField(label="Weight of the product in gm")
    deliveryLocation= forms.IntegerField(label='Delivery Location', widget=forms.Select(choices=DELIVERY_LOCATION))