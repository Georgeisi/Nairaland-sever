from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BlogPost')
    title = models.CharField(max_length=30, null=False) 
    tags = models.CharField(max_length=10,null=False) 
    created_at = models.DateField(auto_now_add=True)  
    story = models.TextField(null=False)
    is_trending= models.BooleanField(default=False)
    image=CloudinaryField('image', )


    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['created_at']
    