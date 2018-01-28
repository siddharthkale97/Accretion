from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/home.html')
    else:
        return redirect('/accounts/login/')
