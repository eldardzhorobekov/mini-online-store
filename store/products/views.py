from django.shortcuts import render
from django.views.generic import DetailView
from products.models import Product

class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product-details.html'