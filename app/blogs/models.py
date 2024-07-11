from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to="blogimg")
    blog_description = models.TextField()
    author = models.CharField(max_length=50)

