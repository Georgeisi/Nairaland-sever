from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BlogPost')
    title = models.CharField(max_length=30, null=False) 
    tags = models.CharField(max_length=10,null=False) 
    created_at = models.DateField(auto_now_add=True)  
    story = models.TextField(null=False)
    