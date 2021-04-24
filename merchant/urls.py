from django.urls import path
from .views import login, order
urlpatterns = [
    path('', login, name='login'),
    path('order',order, name='order')
]
