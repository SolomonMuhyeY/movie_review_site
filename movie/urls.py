from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('<int:movie_id>',views.detail,name='detail'),
  path('<int:movie_id>/create',views.createreview, name='createreview'),
  path('review/<int:review_id>',views.updatereview, name='updatereview'),
  path('review/<int:review_id>/delete',views.deletereview, name='deletereview'),
  path('review/<int:review_id>/vote/', views.vote_review, name='vote_review'),  # Added this line
]