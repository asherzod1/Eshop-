from django.urls import path
from .views import product_detail, store
urlpatterns = [
    path('<int:id>', product_detail, name = 'product_detail'),
    path('', store, name = 'store')
]