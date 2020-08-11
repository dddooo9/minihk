from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product (models.Model):
    title=models.CharField(max_length=50, null=False)
    content=models.TextField()
    price=models.IntegerField(default=0)
    inventory=models.IntegerField(default=0)
    view_count=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/', null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Review(models.Model):
    content=models.TextField()
    grade=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)