from django.contrib import admin
from .models import products, categories

# admin.site.register(products)
# admin.site.register(categories)

@admin.register(categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}