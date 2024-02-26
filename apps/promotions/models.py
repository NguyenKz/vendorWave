from django.db import models

from apps.merchants.models import Merchant

class Promotion(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
