from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet

# Router setup
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]
