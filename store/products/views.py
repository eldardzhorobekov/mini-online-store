from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator
from products.models import Product, Category


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'product'


class CategoryView(DetailView):
    model = Category
    slug_field = 'slug'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        
        context['products'] = Product.objects.filter(category=self.object).per_page(self.request)

        return context