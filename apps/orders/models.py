from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.services.models import Service


class OrderAddress(models.Model):
    name = models.CharField(max_length=255)  # Tên người nhận hàng
    phone = models.CharField(max_length=20)  # Số điện thoại người nhận hàng
    email = models.EmailField()  # Email người nhận hàng
    address = models.TextField()  # Địa chỉ người nhận hàng


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('return', 'Return'),
        ('failed', 'Failed'),
        ('complete', 'Complete'),
        ('validated', 'Validated'),  # Trạng thái mới
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    address = models.ForeignKey(OrderAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    
