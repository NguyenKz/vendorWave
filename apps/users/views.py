from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.request import Request
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request:Request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'detail':'You are alredy login.'})
        
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        response = Response()
        request.session.create()
        session_id = request.session.session_key
        
        response.set_cookie(key="access",value=access_token)
        response.set_cookie(key="refresh",value=refresh_token)
        # response.set_cookie(key="sessionid",value=session_id)
        
        response.data = {
            'access': access_token,
            'refresh': refresh_token,
            # "sessionid":session_id
        }
        response.status_code = status.HTTP_200_OK
        return response


def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            refresh_token = request.COOKIES.get('refresh')
            if refresh_token:
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except Exception as e:
                    pass
            response = Response()
            response.delete_cookie('access')
            response.delete_cookie('refresh')
            response.delete_cookie('sessionid')
            response.data = {'detail': 'Logout successful'}
            logout(request=request)
            return response
        return Response(status=status.HTTP_200_OK)
        