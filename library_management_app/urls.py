from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router for API endpoints
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    # DRF API URLs
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]
