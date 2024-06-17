from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movie,Review,Vote
from .forms import ReviewForm,VoteForm
# Create your views here.
def home(request):
  search_movie =  request.GET.get('search_movie')
  if search_movie:
    movies = Movie.objects.filter(title__icontains = search_movie)
  else:
    movies = Movie.objects.all()
  return render(request,'movie/home.html',{'movies':movies, 'search_movie':search_movie})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from .models import Movie, Vote

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = movie.review_set.all()

    if request.user.is_authenticated:
        for review in reviews:
            review.user_has_upvoted = review.vote_set.filter(user=request.user, vote_type=Vote.UPVOTE).exists()
            review.user_has_downvoted = review.vote_set.filter(user=request.user, vote_type=Vote.DOWNVOTE).exists()
    else:
        for review in reviews:
            review.user_has_upvoted = False
            review.user_has_downvoted = False

    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movie/detail.html', context)


# CREATING A REVIEW
@login_required
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
    
@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie/updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'movie/updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})
@login_required
def vote_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote_type = form.cleaned_data['vote_type']
            existing_vote = Vote.objects.filter(user=request.user, review=review).first()
            
            if existing_vote:
                if existing_vote.vote_type == vote_type:
                    # Remove the vote if it's the same as the existing one (toggle off)
                    existing_vote.delete()
                else:
                    # Change the vote type
                    existing_vote.vote_type = vote_type
                    existing_vote.save()
            else:
                # Create a new vote
                Vote.objects.create(user=request.user, review=review, vote_type=vote_type)
            
            return redirect('detail', movie_id=review.movie.id)
    return redirect('detail', movie_id=review.movie.id)