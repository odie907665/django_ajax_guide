from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.indexView, name="index"),
    path('post/ajax/friend', views.postFriend, name='post_friend'),
    path('get/ajax/validate/nickname', views.checkNickName, name='validate_nickname'),
]