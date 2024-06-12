from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Review
from app.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated

class ReviewListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Extracting book ID from request data
        book_id = request.data.get('book_reviewed')
        if book_id:
            # Check if the user has already reviewed the book
            if Review.objects.filter(reviewed_by=request.user, book_reviewed_id=book_id).exists():
                return Response(
                    {'detail': 'You have already reviewed this book.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(reviewed_by=self.request.user)
