from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#User Model
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no=models.CharField(max_length=12)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'