from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'price', 'image',)


class ProductsInline(admin.TabularInline):
    model = Product
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'slug')
    fields = ('title',)
    inlines = [ProductsInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
