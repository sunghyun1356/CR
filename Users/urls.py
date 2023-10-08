from django.urls import path
from rest_framework_simplejwt import TokenRefreshView
from .views import *

urlpatterns = [
    path('kakao/code/', kakao_login),
    path('login/', KakaoSignUpView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
]