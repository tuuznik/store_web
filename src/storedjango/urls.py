"""storedjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from src.pages.views import (home_view, contact_view, about_view, social_view, cart_add, item_clear,\
                             item_increment, item_decrement, cart_clear, cart_detail) #, cart_buy)
from django.conf.urls import url, include

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('blog/', include('Blog.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('profiles.urls',namespace='profiles')),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/(?P<id>.*0)$/', item_clear, name='item_clear'),
    path('cart/item_increment/(?P<id>.*0)$/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/(?P<id>.*0)$/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    #path('cart/cart-buy/', cart_buy, name='cart_buy'),
]
