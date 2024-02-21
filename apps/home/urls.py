from django.urls import path
from .views import index,about,user_info
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('user_info/', user_info, name='user_info'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]