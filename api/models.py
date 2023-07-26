from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BlogPost')
    title = models.CharField(max_length=30, null=False) 
    tags = models.CharField(max_length=10,null=False) 
    created_at = models.DateField(auto_now_add=True)  
    story = models.TextField(null=False)
    is_trending= models.BooleanField(default=False)
    image= CloudinaryField('image', null=True ,blank=True )


    def __str__(self):
        return self.title 
    
    class Meta:
        ordering= ['created_at']
    # @property
    # def image_url(self):
    #     return (
    #         f"https://res.cloudinary.com/dpoix2ilz/{self.image}"
    #     )