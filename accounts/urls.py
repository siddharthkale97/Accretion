from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login/', login, {'template_name': 'accounts/login.html'}),
]