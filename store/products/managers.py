from django.core.paginator import Paginator
from django.db import models


class PageQuerySet(models.QuerySet):
    def per_page(self, request, per_page=8):
        paginator = Paginator(self, per_page)
        page_number = request.GET.get('page', 1)
        return paginator.get_page(page_number)

ProductManager = models.Manager.from_queryset(PageQuerySet)