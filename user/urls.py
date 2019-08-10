from django.conf.urls import url
from django.contrib.auth import logout

from user.views import signup

urlpatterns = [

    url(r'^signup/$',signup, name='signup'),
    url(r'^logout/$', logout, name='logout'),
]
