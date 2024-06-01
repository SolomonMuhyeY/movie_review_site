from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movie,Review
from .forms import ReviewForm
# Create your views here.
def home(request):
  movies = Movie.objects.all()
  return render(request,'movie/home.html',{'movies':movies})
def detail(request,movie_id):
  movie = get_object_or_404(Movie,pk=movie_id)
  reviews = Review.objects.filter(movie = movie)
  return render(request,'movie/detail.html',{'movie':movie, 'reviews':reviews})

# CREATING A REVIEW
# @login_required
def createreview(request,movie_id):
  movie = get_object_or_404(Movie, pk= movie_id)
  if request.method == 'GET':
    return render(request,'movie/createreview.html',{'movie':movie, 'form': ReviewForm})
  else:
    try:
      form = ReviewForm(request.POST)
      newReview = form.save(commit=False)
      newReview.user = request.user
      newReview.movie = movie
      newReview.save()
      return redirect('detail',newReview.movie.id)
    except ValueError:
     return render(request,'movie/createreview.html', {'form':ReviewForm(),'error':'bad data passed in'})
# @login_required
def deletereview(request,review_id):
  review = get_object_or_404(Review, pk = review_id, user= request.user)
  if request.method == 'POST':
    review.delete()
    return redirect('detail', movie_id = review.movie.id)
  return render(request,'movie/confirm_delete.html',{'review':review})
    
