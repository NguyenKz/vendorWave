# views.py
# Trong tệp views.py của ứng dụng của bạn
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product  # Thay thế Product bằng tên model sản phẩm của bạn
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from .forms import ProductForm
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@login_required  # Đảm bảo rằng người dùng đã đăng nhập mới có thể truy cập trang này
def my_products_view(request):
    user_products = Product.objects.filter(merchant=request.user.merchant)
    return render(request, 'my_products.html', {'user_products': user_products})



class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({'detail': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)