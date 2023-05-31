from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path("register", RegisterAPIView.as_view()),  # post 요청만 처리함
    path("auth", AuthView.as_view()),  # 회원 권한 검증
    path("login", LoginView.as_view()),  # 로그인
]
