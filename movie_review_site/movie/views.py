from django.shortcuts import get_object_or_404, render
from .models import Movie
# Create your views here.
def home(request):
  movies = Movie.objects.all()
  return render(request,'movie/home.html',{'movies':movies})
def detail(request,movie_id):
  movie = get_object_or_404(Movie,pk=movie_id)
  return render(request,'movie/detail.html',{'movie':movie})