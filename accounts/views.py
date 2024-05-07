from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, SignupForm, EditProfileForm
from .models import CustomUser


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else: # the form is invalid there is an issue/s
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field} : {error}")
        
    else: # the user method is get  
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"{user.username} has logged in successfully")
            return redirect('profile')

        else: # the form is invalid there is an issue/s
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field} : {error}")

    else: # the user method is get  
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', context={'user':request.user})

@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field} : {error}")
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'accounts/editProfile.html', context={'form': form, 'user':request.user})