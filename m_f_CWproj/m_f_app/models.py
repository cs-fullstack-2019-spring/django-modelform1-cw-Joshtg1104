from django.db import models
from django.utils import timezone


# Create your models here.
# Model that allows users to enter blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
