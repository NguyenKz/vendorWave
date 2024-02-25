# urls.py

from django.urls import path
from .views import CreateProductAPIView, ProductDeleteAPIView, my_products_view

urlpatterns = [
    path('create/', CreateProductAPIView.as_view(), name='create_product_api'),
    path('my-products/', my_products_view, name='my_products'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete-api'),
    # Các URL khác của ứng dụng
]
