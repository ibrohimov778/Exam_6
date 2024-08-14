from django.contrib import admin
from django.urls import path
from customer.views.views import customer_list
from customer.views import views
from customer.views.views import customer_detail

urlpatterns = [
    path('customer-list/', customer_list, name='customer_list'),
    path('customer-detail/<int:product_id>/', views.customer_detail, name='customer_detail'),
]
