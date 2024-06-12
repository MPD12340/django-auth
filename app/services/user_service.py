from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from app.accessors import UserAccessor
from django.contrib.auth.hashers import make_password


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserService:

    @staticmethod
    def user_login(email, password):
        user = authenticate(email=email, password=password)
        if user is not None:
            return get_tokens_for_user(user)
        return None

    @staticmethod
    def register_user(register_data):
        # Hash the password before passing the data to the register method
        register_data["password"] = make_password(register_data["password"])
        user = UserAccessor.register(register_data)
        return user
