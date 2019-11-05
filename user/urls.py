from django.conf.urls import url
from django.contrib.auth import logout
from django.urls import path

from user.views import signup, UserLoginView, UserRegisterView

app_name = 'user'

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('login-register/', UserLoginView.as_view(), name='login_register'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
