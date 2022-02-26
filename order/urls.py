from django.urls import path
from .views import add_cart, orders_cart
urlpatterns = [
    path('add-cart/', add_cart, name ='add_cart'),
    path('items/', orders_cart, name ='orders_cart')
]