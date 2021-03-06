from django.urls import path

from tweets import views
from tweets.views import ComposeTweet, DeleteTweet, TweetDetail, TweetList, FollowersList, FollowingList, EditTweet, UserTweetList

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TweetList.as_view(), name='home'),
    path('tweet/compose/', ComposeTweet.as_view(), name='compose-tweet'),
    path('tweet/<int:pk>/', TweetDetail.as_view(), name='tweet-detail'),
    path('tweet/<int:pk>/delete/', DeleteTweet.as_view(), name='delete-tweet'),
    path('tweet/<int:pk>/edit/', EditTweet.as_view(), name='edit-tweet'),
    path('user/<str:username>/', UserTweetList.as_view(), name='user-tweet-list'),
    path('user/<str:username>/following', FollowingList.as_view(), name='following'),
    path('user/<str:username>/followers', FollowersList.as_view(), name='followers'),
]
