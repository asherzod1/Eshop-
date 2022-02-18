from django.contrib import admin

from product.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    list_display = ['id', 'name', 'price', 'quantity']

class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    list_display = ['name']
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
