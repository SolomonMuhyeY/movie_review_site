from django.urls import path
from . import views

urlpatterns = [
  path('signup/',views.signup, name='signup'),
  path('login/',views.loginaccount, name='login'),
  path('logout/',views.logoutaccount, name='logout'),
  path('profile/',views.profile, name='profile'),
  path('edit_profile/', views.update_profile_image, name='update_profile_image'),
]