from django.urls import path, include
from .views import user_profile, sign_up

app_name = 'profiles'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile', user_profile, name='profile-detail'),
    path('sign_up/', sign_up, name='sign_up'),]
    # path('<int:product_id>/', product_detail_view, name='product-detail'),
    # path('<int:product_id>/update/', product_update_view, name='product-update'),
    # path('<int:product_id>/delete/', product_delete_view, name='product-delete')]