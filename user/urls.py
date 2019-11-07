from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import signup, UserLoginView, UserRegisterView

app_name = 'user'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
