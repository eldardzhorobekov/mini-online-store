from django.db import models
from products.helpers import slugify


DEFAULT_CATEGORY_SLUG = 'no-categories'

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categories'


class Product(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url if self.image else '/media/products/default.jpg'

    def def_category_slug(self):
        return self.category.slug if self.category else DEFAULT_CATEGORY_SLUG
