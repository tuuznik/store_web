from django.urls import path
from .views import item_update_view, warehouse_list_view

app_name = 'warehouse'
urlpatterns = [
    path('', warehouse_list_view, name='warehouse-list'),
    path('<int:item_id>/update/', item_update_view, name='item-update'),]
    # path('<int:product_id>/', product_detail_view, name='product-detail'),
    # path('<int:product_id>/update/', product_update_view, name='product-update'),
    # path('<int:product_id>/delete/', product_delete_view, name='product-delete')]
