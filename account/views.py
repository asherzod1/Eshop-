from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.models import Customer
from product.models import Product

def log_in(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password', None)
        customer = authenticate(phone_number=phone_number, password=password)
        if customer:
            login(request=request, user=customer)
            return redirect('home')
    return render(
        request=request,
        template_name='pages/signin.html'
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def home(request):
    products = Product.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={
            'products': products
        }
    )


def register(request):
    phone_number_error: str = ''
    password_error: str = ''
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        customer: Customer = Customer.objects.filter(phone_number=phone_number)
        if customer:
            phone_number_error = 'This phone number is already used'
        elif password != password1:
            password_error = 'Check your passwords'
        else :
            new_customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                phone_number=phone_number,
                password=password
            )
            new_customer.set_password(password)
            new_customer.save()
            if new_customer:
                login(request, new_customer)
            return redirect('home')
    return render(
        request=request,
        template_name='pages/register.html',
        context={
            'phone_number_error': phone_number_error,
            'password_error': password_error
        }
    )
