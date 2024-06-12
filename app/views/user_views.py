from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app.serializers import LoginSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from app.services import UserService
from app.builders import ResponseBuilder, api


@swagger_auto_schema(method="post", request_body=LoginSerializer, responses={200: "OK"})
@api_view(["POST"])
def login_view(request):
    response_builder = ResponseBuilder()
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        tokens = UserService.user_login(email, password)
        if tokens:
            # return Response(tokens, status=status.HTTP_200_OK)
            return response_builder.get_200_success_response('user logged in successfully', tokens)
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    request_body=RegisterSerializer,
    responses={201: "Created"},
)
@api_view(["POST"])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        UserService.register_user(serializer.validated_data)
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method="get", responses={200: "OK"})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "I am protected"}, status=status.HTTP_200_OK)
