from django.contrib.auth import get_user_model
from rest_framework import serializers
from app.models import Book, CustomUser
from .review_serializer import ReviewSerializer


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    publication_date = serializers.DateField()
    image = serializers.ImageField(required=False, allow_null=True)
    is_deleted = serializers.BooleanField(default=False)
    published_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date
        )
        instance.image = validated_data.get("image", instance.image)
        instance.is_deleted = validated_data.get("is_deleted", instance.is_deleted)
        instance.published_by = validated_data.get(
            "published_by", instance.published_by
        )
        instance.save()
        return instance
