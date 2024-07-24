from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog_name = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to="blogimg")
    blog_description = models.TextField()
    author = models.CharField(max_length=50)

