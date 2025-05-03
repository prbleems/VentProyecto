from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('',             ProductListView.as_view(),   name='product_list'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
