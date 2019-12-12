from django.shortcuts import render, get_object_or_404
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


def home(request):
    return render(request, 'tweets/home.html', context={})


class ComposeTweet(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['content']
    template_name = 'tweets/compose_tweet.html'
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['header'] = 'Compose a new tweet'
        return data


class DeleteTweet(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_tweet.html'
    success_url = '/home'
    context_object_name = 'tweet'

    def test_func(self, **kwargs):
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
