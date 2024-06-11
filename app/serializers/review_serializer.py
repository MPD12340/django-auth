from rest_framework import serializers
from app.models import Review, CustomUser, Book


class ReviewSerializer(serializers.Serializer):
    review_message = serializers.CharField()
    rating = serializers.ChoiceField(
        choices=[
            (1, "1 star"),
            (2, "2 stars"),
            (3, "3 stars"),
            (4, "4 stars"),
            (5, "5 stars"),
        ]
    )
    reviewed_by = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), allow_null=True
    )
    book_reviewed = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.review_message = validated_data.get(
            "review_message", instance.review_message
        )
        instance.rating = validated_data.get("rating", instance.rating)
        instance.reviewed_by = validated_data.get("reviewed_by", instance.reviewed_by)
        instance.book_reviewed = validated_data.get(
            "book_reviewed", instance.book_reviewed
        )
        instance.save()
        return instance
