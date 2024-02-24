from django.db import models
from apps.merchants.models import Merchant


class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm
    sku = models.CharField(max_length=255)  # SKU (Stock Keeping Unit)
    brand = models.CharField(max_length=255)  # Thương hiệu
    model = models.CharField(max_length=255)  # Model
    quantity = models.PositiveIntegerField(default=0)  # Số lượng tồn kho
    image = models.ImageField(upload_to='product_images/')  # Trường hình ảnh sản phẩm
    # Other product-related fields
