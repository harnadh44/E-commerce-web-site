from django.contrib import admin
from .products import Product
from .category import Category


class CategoryName(admin.ModelAdmin):
    list_display = ["name"]

class ProductName(admin.ModelAdmin):
    list_display = ["name", "category", "price"]

# Register your models here.
admin.site.register(Product, ProductName)
admin.site.register(Category, CategoryName)