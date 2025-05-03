# catalog/views.py
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 12
    template_name = 'catalog/product_list.html'
    # opcional: context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    # opcional: context_object_name = 'product'
