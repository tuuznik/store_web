from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
from warehouse.models import Item


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save()
        Item.objects.create(product=product, quantity=0)
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


# modifying existing products
def product_update_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=obj) # initial=initial_data
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)