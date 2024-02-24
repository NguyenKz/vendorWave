from django.db import models
from apps.merchants.models import Merchant


class Service(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Tên dịch vụ
    description = models.TextField()  # Mô tả dịch vụ
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá dịch vụ
    quantity = models.PositiveIntegerField(default=0)  # Số lượng dịch vụ
    image = models.ImageField(upload_to='service_images/')  # Trường hình ảnh dịch vụ
    # Other service-related fields
