from django.core.paginator import Paginator
from django.shortcuts import render

from product.models import Product, Category


def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(
        request=request,
        template_name='pages/product_detail.html',
        context={
            'product':product
        }
    )

def store(request):
    category = (request.GET.get('category', None))
    min_price = (request.GET.get('min_price', None))
    max_price = (request.GET.get('max_price', None))
    paginator_page:str = request.GET.get('page', '1')
    per_page:str = request.GET.get('per-page',6)
    if category:
        product_list = Product.objects.filter(category_id=category)
    else:
        product_list = Product.objects.all()
    if min_price:
        product_list = Product.objects.filter(price__gte=min_price)
    if max_price:
        product_list = Product.objects.filter(price__lte=max_price)
    categories = Category.objects.all()
    paginator = Paginator(
        object_list=product_list,
        per_page=per_page,

    )

    product_list_page = paginator.get_page(paginator_page)
    paginator_page = int(paginator_page) if paginator_page.isdigit() else 1
    paginator_page = paginator_page if paginator_page<=paginator.num_pages else paginator.num_pages
    return render(
        request=request,
        template_name='pages/store.html',
        context={
            'products': product_list_page,
            'categories': categories,
            'paginator' : paginator,
            'current_page' : int(paginator_page),
        }
    )

def search(request):
    search_value = (request.GET.get('search_input'))
    print(search_value)
    products = Product.objects.filter(name__contains=search_value)
    categories = Category.objects.all()
    return render(
        request=request,
        template_name='pages/store.html',
        context={
            'products': products,
            'categories': categories
        }
    )