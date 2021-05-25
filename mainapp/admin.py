from django.contrib import admin
from mainapp.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'quantity')
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)