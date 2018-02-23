from django.urls import path, include
from homepage.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
]