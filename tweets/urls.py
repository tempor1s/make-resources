from django.urls import path

from tweets import views
from tweets.views import ComposeTweet

urlpatterns = [
    path('', views.index, name='homepage'),
    path('home/', views.home, name='home'),
    path('tweet/compose/', ComposeTweet.as_view(), name='compose')
]
