from django.urls import path
from .views import RegisterView, LoginView,sign_in,LogoutView,sign_up

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('sign-up/', sign_up, name='sign_up'),
    path('token/', LoginView.as_view(), name='login'),
    path('login/', sign_in, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
