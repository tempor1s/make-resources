from django.urls import path

from tweets import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('home/', views.home, name='home')
]
