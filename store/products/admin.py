from django.contrib import admin
from django.db.models import Count
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'price', 'image',)


class ProductsInline(admin.TabularInline):
    model = Product
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'slug', 'books_count')
    fields = ('title',)
    inlines = [ProductsInline]
    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.annotate(product_count=Count('products'))

    def books_count(self, instance):
        return instance.product_count

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
