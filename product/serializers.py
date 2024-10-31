from rest_framework import serializers
from .models import Product, Stock


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Includes all fields in the Product model


# Stock Serializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'  # Includes all fields in the Stock model
