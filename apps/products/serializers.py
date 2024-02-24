# Trong tệp serializers.py
from rest_framework import serializers
from .models import Product
from rest_framework.exceptions import APIException
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "price","sku","brand","model","image"
        )
    
    def validate(self, attrs):
        if hasattr(self.context["request"].user,"merchant"):
            attrs["merchant"]=self.context["request"].user.merchant
        else:
            raise APIException(detail="Something was wrong.")
        
        return super().validate(attrs)
        
    
