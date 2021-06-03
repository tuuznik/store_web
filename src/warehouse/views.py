from django.shortcuts import render, get_object_or_404, reverse
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect
# Create your views here.

def item_update_view(request, item_id):
    obj = get_object_or_404(Item, id=item_id)
    form = ItemForm(request.POST or None, instance=obj) # initial=initial_data
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "warehouse/item_update.html", context)

def  warehouse_list_view(request):
    queryset = Item.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "warehouse/warehouse_list.html", context)