from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from .models import products, categories, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']

    inlines = [CartTabAdmin, OrderTabulareAdmin]

@admin.register(categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]

@admin.register(products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'quantity', 'product_price', 'discount']
    list_editable = ['product_price', 'discount']
    search_fields = ['product_name','description']
    list_filter = ['category', ]
    fields = [
        'product_name',
        'category',
        'description',
        ('product_price', 'discount'),
        'quantity',
        'img',
        'slug'
    ]