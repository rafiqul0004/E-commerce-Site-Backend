from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

# Router setup
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]
