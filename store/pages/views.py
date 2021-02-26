from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from products.models import Product


class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        product_list = Product.objects.all()
        paginator = Paginator(product_list, 8)
        page_number = self.request.GET.get('page', 1)
        context['products'] = paginator.get_page(page_number)
        
        return context