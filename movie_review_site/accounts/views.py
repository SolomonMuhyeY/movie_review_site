from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProfile
from .forms import UserCreateForm ,UserProfileForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST,request.FILES)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user =form.save()
                    login(request,user)
                    return redirect('home')
                except IntegrityError:
                    form.add_error()
            else:
                form.add_error()
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return render(request, 'accounts/signup.html', {'form': UserCreateForm})  
def loginaccount(request):
    if request.method == 'GET':
        return render(request,'accounts/login.html',{'form':AuthenticationForm} )
    else:
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.POST['password'],                       
                            )
        
        if user  is None:
            return render(request,'accounts/login.html',{'form':AuthenticationForm(),'error':'User name and password does\'t match.'})
        else:
            login(request,user)
            return redirect('home')

@login_required
def logoutaccount(request):
  logout(request)
  return redirect('home')
def profile(request):
    user_profile = UserProfile.objects.get(user = request.user)
    context = {'user_profile':user_profile}
    return render(request,'accounts/profile.html',context)
@login_required
def update_profile_image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.image = form.cleaned_data['image']
            user_profile.hobby = form.cleaned_data['hobby']
            user_profile.genre = form.cleaned_data['genre']
            user_profile.save()
            return redirect('home')  # Redirect to the profile page after updating
    else:
        form = UserProfileForm()
    return render(request, 'accounts/edit_profile.html', {'form': form})

             
