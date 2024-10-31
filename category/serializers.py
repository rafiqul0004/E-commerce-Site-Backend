from rest_framework import serializers
from .models import Category

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Includes all fields in the Category model