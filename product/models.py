from django.db import models
from category.models import Category

# Create your models here.
class Size(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    name = models.CharField(max_length=2, choices=SIZE_CHOICES, unique=True)  # Unique constraint for each size

    def __str__(self):
        return self.get_name_display()
# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, related_name='products')
    sizes = models.ManyToManyField(Size, related_name='products')  # 'S', 'M', 'L', 'XL'
    image = models.ImageField(upload_to='products/media/upload', blank=True, null=True)

    def __str__(self):
        return self.name

# Stock Model
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"