from django.conf.urls import *
from django.urls import path
from .views import login, order
from django.conf import settings


urlpatterns = [
    path('', login, name='login'),
    path('order',order, name='order')
]
