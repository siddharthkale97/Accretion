from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/home.html')
    else:
        return redirect('/accounts/login/')


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
