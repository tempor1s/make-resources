from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import register, update_profile
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', update_profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
