from django.urls import path
from app.views import login_view, register_view, protected_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="login"),
    path("protect/", protected_view, name="protect"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
