from django.db import models

# Create your models here.

#Model for Category

class Category(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField()

    def __str__(self) -> str:
        return self.name
