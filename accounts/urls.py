from django.urls import path
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('reset-password', password_reset, name='password-reset'),
    path('reset-password/done', password_reset_done, name='password_reset_done'),
    path('reset-password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/complete', password_reset_complete, name='password_reset_complete'),
]

# USE THIS FOR EMAIL SERVER CHANGE THIS WHILE DEPLOYMENT python -m smtpd -n -c DebuggingServer localhost:1025
