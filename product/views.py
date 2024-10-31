from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
# Create your views here.

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Stock ViewSet
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
