from django.urls import path

from tweets import views
from tweets.views import ComposeTweet, DeleteTweet, TweetDetail, TweetList, FollowersList, FollowingList

urlpatterns = [
    path('', views.index, name='homepage'),
    path('home/', TweetList.as_view(), name='home'),
    path('tweet/compose/', ComposeTweet.as_view(), name='compose-tweet'),
    path('tweet/<int:pk>/', TweetDetail.as_view(), name='tweet-detail'),
    path('tweet/<int:pk>/delete/', DeleteTweet.as_view(), name='delete-tweet'),
    path('user/<str:username>/following', FollowingList.as_view(), name='following'),
    path('user/<str:username>/followers', FollowersList.as_view(), name='followers')
]
