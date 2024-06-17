from django.db import models

# Create your models here.
class News(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=30)
  description = models.TextField()
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True, editable=True)
  image = models.ImageField(upload_to='news/image')
  
def __str__(self):
  return self.text
    