from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Post_By(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    

class Post(models.Model):
    post_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    extract = models.TextField()
    content = models.TextField()
    posted_by = models.ForeignKey(Post_By,on_delete=models.CASCADE,null=True)
    
    
    
    
    slug = models.SlugField(default='',db_index=True)
    
    image = models.ImageField(upload_to='images')
    imagesecond=models.ImageField(upload_to='images')
    imagethird=models.ImageField(upload_to='images')
    
    def get_absolute_url(self):
        return reverse("allposts", args=[self.slug])
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.post_name)                                           
        super().save(*args, **kwargs)
        
        
        
    def __str__(self):
        return f'{self.title} and {self.post_name}'
    