
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserInfoView, UserRegistrationView, LoginView, LogoutView, CookieTokenRefreshView

urlpatterns = [
    path("user-info/", UserInfoView.as_view(), name="user-info"),
    path("register/", UserRegistrationView.as_view(), name="register-user"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("logout/", LogoutView.as_view(), name="user-logout"),
    path("refresh/", CookieTokenRefreshView.as_view(), name="token-refresh"),
]
