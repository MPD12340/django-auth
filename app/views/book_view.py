from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Book
from app.serializers import BookSerializer
from app.utils import CustomIsAuthenticated
from rest_framework.permissions import IsAuthenticated
from app.services import BookService
from app.builders import ResponseBuilder
from rest_framework.decorators import api_view, permission_classes


# response =
class BookListCreateAPIView(APIView):
    # permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        response_builder = ResponseBuilder()
        books = BookService.get_all_books()
        serializer = BookSerializer(books, many=True)
        return response_builder.get_200_success_response(
            "books retrieved successfully", serializer.data
        )
@permission_classes([CustomIsAuthenticated])
def post(self, request):
    request.data["published_by"] = request.user.id
    serializer = BookSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)



class BookDetailAPIView(APIView):
    permission_classes = [CustomIsAuthenticated]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book.published_by != request.user:
            return Response(
                {"detail": "You do not have permission to edit this book."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book.published_by != request.user:
            return Response(
                {"detail": "You do not have permission to delete this book."},
                status=status.HTTP_403_FORBIDDEN,
            )

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
