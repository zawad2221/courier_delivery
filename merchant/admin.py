from django.contrib import admin
from .models import ProductType, Merchant, MerchantInvoice, Order

admin.site.register(ProductType)
admin.site.register(Merchant)
admin.site.register(MerchantInvoice)
admin.site.register(Order)
