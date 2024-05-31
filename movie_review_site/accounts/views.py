from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        email='default@gmail.com'
                    )
                    user.save()
                    login(user)
                    return redirect('home')
                except IntegrityError:
                    err_msg = "Username already exists. Please choose a different username."
                    return render(request, 'accounts/signup.html', {'form': form, 'err_msg': err_msg})
            else:
                err_msg = "Passwords do not match."
                return render(request, 'accounts/signup.html', {'form': form, 'err_msg': err_msg})
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
        if user is None:
            return render(request,'accounts/login.html',{'form':AuthenticationForm(),'error':'User name and password does\'t match.'})
        else:
            login(request,user)
            return redirect('home')

@login_required
def logoutaccount(request):
  logout(request)
  return redirect('home')