from rest_framework import serializers
from .models import Author, Book, Member

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth']

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn_number', 'available_copies']

    def create(self, validated_data):
        author_data = validated_data.pop('author')  # Extract author data
        author = Author.objects.create(**author_data)  # Create the author instance
        book = Book.objects.create(author=author, **validated_data)  # Create the book instance
        return book

# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'joined_date', 'active']
