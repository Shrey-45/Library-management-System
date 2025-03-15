from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Index page view
def index(request):
    return render(request, 'library_management_app/index.html')

# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    @action(detail=True, methods=['get'])
    def get_authors(self, request, pk=None):
        """
        Custom action to retrieve authors of a specific book
        """
        book = self.get_object()
        authors = book.authors.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

# Author ViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing author instances.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
