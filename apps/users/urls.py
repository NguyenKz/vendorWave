from django.urls import path
from .views import RegisterView, LoginView,sign_in,LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', LoginView.as_view(), name='login'),
    path('login/', sign_in, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
