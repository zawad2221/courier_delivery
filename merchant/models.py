from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey


class ProductType(models.Model):
    PRODUCT_TYPE = (
        ('Fragile','Fragile'),
        ('Liquid','Liquid')
    )
    typeName = CharField(max_length=11, choices=PRODUCT_TYPE)
    def __str__(self):
        return self.typeName

class Merchant(models.Model):
    name = CharField(max_length=22)
    def __str__(self):
        return self.name

class MerchantInvoice(models.Model):
    merchantId = ForeignKey(Merchant, on_delete=models.CASCADE)

class Order(models.Model):
    DELIVERY_LOCATION = (
        (0,'Inside of Dhaka'),
        (1,'Division of Dhaka'),
        (2,'Outside of Dhaka')
    )
    deliveryLocation = IntegerField(choices=DELIVERY_LOCATION)
    invoiceId = ForeignKey(MerchantInvoice, on_delete= models.CASCADE)
    weight = FloatField()
    charge = FloatField()
    type = ForeignKey(ProductType, on_delete=models.CASCADE, default=1)