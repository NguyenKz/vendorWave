from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        response = Response()
        response.set_cookie(key="access",value=access_token)
        response.set_cookie(key="refresh",value=refresh_token)
        
        response.data = {
            'access': access_token,
            'refresh': refresh_token,
        }
        response.status_code = status.HTTP_200_OK
        return response


def sign_in(request):
    return render(request, 'sign_in.html')