from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from products.models import Product
from warehouse.models import Item
from django.db import transaction
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    about_info = {
        "text": "admin username",
        "my_number": 123,
        "my_list": [43, 12, 5]
    }
    return render(request, 'about.html', about_info)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    with transaction.atomic():
        product = Product.objects.select_for_update().get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    if cart.cart[str(id)]['quantity'] == 1:
        cart.remove(product)
    else:
        cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = Cart(request)
    context = {
        'object': cart
    }
    return render(request, "cart/cart_detail.html", context)
    #return render(request, 'cart/cart_detail.html')

@login_required(login_url="/accounts/login/")
def cart_buy(request):
    cart = Cart(request)
    cart.buy()
    cart.clear()
    return redirect("home")