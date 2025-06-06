# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.order_checkout,    name='order_checkout'),
    path('payment/',  views.payment,           name='payment'),
    path('finish/',   views.order_finish,      name='order_finish'),
]
