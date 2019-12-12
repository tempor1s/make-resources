from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from tweets.models import Tweet, Reply
from users.models import Follower, Profile
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count

from tweets.forms import NewReplyForm  # new reply form (tweet response)

# helper func to make sure that the post's user is the logged in user, so that people can not delete/edit other users tweet


def is_logged_user(post_user, logged_user):
    return post_user == logged_user


def index(request):
    return render(request, 'tweets/index.html', context={})


class ComposeTweet(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['content']
    template_name = 'tweets/compose_tweet.html'
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteTweet(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_tweet.html'
    success_url = '/home'
    context_object_name = 'tweet'

    def test_func(self, **kwargs):
        return is_logged_user(self.get_object().author, self.request.user)


class EditTweet(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tweet
    fields = ['content']
    template_name = 'tweets/edit_tweet.html'
    success_url = '/home'

    def get_success_url(self):
        return reversed

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return is_logged_user(self.get_object().author, self.request.user)


class TweetDetail(LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = 'tweets/tweet_detail.html'
    context_object_name = 'tweet'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        replies = Reply.objects.filter(
            tweet_connected=self.get_object()).order_by('-date_posted')
        data['replies'] = replies
        data['form'] = NewReplyForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_reply = Reply(content=request.POST.get('content'),
                          author=self.request.user,
                          tweet_connected=self.get_object())
        new_reply.save()

        return self.get(self, request, *args, **kwargs)


# class AllTweets(LoginRequiredMixin, ListView):
#     model = Tweet
#     template_name = 'tweets/all_tweets.html'
#     context_object_name = 'tweets'
#     ordering = ['-date_posted']
#     paginate_by = 20


class TweetList(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'tweets/home.html'
    context_object_name = 'tweets'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data_counter = Tweet.objects.values('author').annotate(author_count=Count('author')).order_by('-author_count')[:5]

        data['all_users'] = [User.objects.filter(pk=aux['author']).first() for aux in data_counter]
        return data

    def get_queryset(self):
        user = self.request.user
        query_set = Follower.objects.filter(user=user)
        followers = [user]
        for obj in query_set:
            followers.append(obj.following_user)
        
        return Tweet.objects.filter(author__in=followers).order_by('-date_posted')
    

class FollowingList(ListView):
    model = Follower
    template_name = 'tweets/follow_page.html'
    context_object_name = 'following'

    def visable_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))
    
    def get_queryset(self):
        user = self.visable_user()
        return Follower.objects.filter(user=user).order_by('-date_followed')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow_type'] = 'following'
        return data


class FollowersList(ListView):
    model = Follower
    template_name = 'tweets/follow_page.html'
    context_object_name = 'followers'

    def visable_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visable_user()
        return Follower.objects.filter(following_user=user).order_by('-date_followed')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow_type'] = 'followers'
        return data