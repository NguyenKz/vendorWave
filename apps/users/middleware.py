# middleware.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
User = get_user_model()
class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def push_user(self,request:WSGIRequest):
        # access = request.COOKIES.get("access")
        # refresh = request.COOKIES.get("refresh")
        # try:
        #     data = AccessToken(access)
            
        #     user = User.objects.get(pk=data.payload["user_id"])
        #     request.user = user
        # except:
        #     pass
        response = self.get_response(request)
        return response
    
    def __call__(self, request:WSGIRequest):
        return self.push_user(request=request)

