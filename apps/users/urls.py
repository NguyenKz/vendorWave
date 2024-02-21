from django.urls import path
from .views import sign_up, sign_in

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
]