from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('products/<int:pk>', views.ProductDetailsView.as_view(), name='product-details'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
]
