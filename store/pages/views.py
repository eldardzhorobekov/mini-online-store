from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from products.models import Product, Category


class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all().per_page(self.request)

        return context