from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.forms import RegistrationForm, Editprofile
from django.contrib.auth.models import User
# Create your views here.

def register(request):

     if request.user.is_authenticated:
         return redirect('/accounts/home')
     else:
         if request.method == 'POST':
             form = RegistrationForm(request.POST)
             if form.is_valid():
                 form.save()
                 return redirect('/accounts/home/')
         else:
             form = RegistrationForm()
             args = {'form': form}
             return render(request, 'accounts/reg_form.html', args)

def home(request):

    if request.user.is_authenticated:
        return render(request, 'accounts/home.html')
    else:
        return redirect('/accounts/login/')

def view_profile(request):

    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):

    if request.method == 'POST':
        form = Editprofile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = Editprofile(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)