from django.contrib import admin
from django.urls import path
from butchery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products_page, name='products'),
    path('contact/', views.contact, name='contact'),
    path('orders/', views.order, name='order'),
]
