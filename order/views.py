import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from order.models import Order, Order_detail
from product.models import Product
from utilits.utilits import get_order_count


def add_cart(request):
    if request.method == "POST":
        data:dict = json.loads(request.body)
        product = Product.objects.get(id=data['product_id'])
        user_orders = request.user.orders.all().order_by('-id')
        if user_orders:
            order = user_orders.first()
        else:
            order = Order.objects.create(
                customer=request.user
            )
        order_detail = Order_detail.objects.filter(
            order=order,
            product=product
        )
        if order_detail:
            order_detail.delete()
        else:
            order_detail = Order_detail.objects.create(
                order=order,
                product=product
            )

    return JsonResponse({"items_count": order.items_count()})

def orders_cart(request):
    badge_count = get_order_count(request)
    order = request.user.orders.order_by('-id').first()
    return render(
        request=request,
        template_name='pages/orders_cart.html',
        context = {
            'badge_count':badge_count,
            'order':order
        }
    )
