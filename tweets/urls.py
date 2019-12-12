from django.urls import path

from tweets import views
from tweets.views import ComposeTweet, DeleteTweet, TweetDetail

urlpatterns = [
    path('', views.index, name='homepage'),
    path('home/', views.home, name='home'),
    path('tweet/compose/', ComposeTweet.as_view(), name='compose-tweet'),
    path('tweet/<int:pk>/', TweetDetail.as_view(), name='tweet-detail'),
    path('tweet/<int:pk>/delete/', DeleteTweet.as_view(), name='delete-tweet'),
]
