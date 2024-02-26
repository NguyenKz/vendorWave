from django.urls import path
from .views import CreatePromotionAPIView, my_promotions_view, PromotionDeleteAPIView

urlpatterns = [
    path('create/', CreatePromotionAPIView.as_view(), name='create-promotion'),
    path('my-promotions/', my_promotions_view, name='my-promotions'),
    path('delete/<int:pk>/', PromotionDeleteAPIView.as_view(), name='delete-promotion'),
]
