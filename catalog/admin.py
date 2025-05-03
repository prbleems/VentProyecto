from django.contrib import admin
from .models import Category, Size, Color, Product, ProductImage

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductImage)
