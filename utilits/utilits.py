def get_order_count(request):
    if request.user.is_authenticated:
        if request.user.orders.all():
            return request.user.orders.all().order_by('-id').first().details.count()
        else:
            return 0