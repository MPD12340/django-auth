from django.urls import path
from app.views import login_view, register_view, protected_view
from rest_framework_simplejwt.views import TokenRefreshView
from app.views import BookListCreateAPIView, BookDetailAPIView, ReviewListCreateAPIView

urlpatterns = [
    # auth
    path("login/", login_view, name="login"),
    path("register/", register_view, name="login"),
    path("protect/", protected_view, name="protect"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # books
    path("book/", BookListCreateAPIView.as_view(), name="list-create"),
    path("book/<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),
    # reviews
    path("review/", ReviewListCreateAPIView.as_view(), name="review-list-create"),
]
