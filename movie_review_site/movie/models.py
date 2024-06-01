from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True)
  author = models.CharField(max_length=30)
  description = models.TextField()
  image = models.ImageField(upload_to='movie/images')
  trailers = models.TextField(null=True)
  
def __str__(self):
  return self.title


class Review(models.Model):
  review_text = models.TextField()
  date = models.DateTimeField(auto_now_add=True, editable=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
  def __str__(self):
    return self.review_text[:50]