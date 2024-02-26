from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Promotion
from .serializers import PromotionSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CreatePromotionAPIView(generics.CreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@login_required(login_url="/user/login/")
def my_promotions_view(request):
    user_promotions = Promotion.objects.filter(merchant=request.user.merchant)
    return render(request, 'my_promotion.html', {'user_promotions': user_promotions})

class PromotionDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            promotion = Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            return Response({'detail': 'Promotion not found'}, status=status.HTTP_404_NOT_FOUND)

        promotion.delete()
        return Response({'detail': 'Promotion deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
