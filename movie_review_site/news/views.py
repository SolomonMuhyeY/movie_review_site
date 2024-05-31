from django.http import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
  newss = News.objects.all()
  return render(request,'news/news.html',{'newss':newss})