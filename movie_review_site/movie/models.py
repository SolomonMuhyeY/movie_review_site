from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True)
  author = models.CharField(max_length=30)
  description = models.TextField()
  image = models.ImageField(upload_to='movie/images')
  trailers = models.TextField(null=True)
  
def __str__(self):
  return self.text