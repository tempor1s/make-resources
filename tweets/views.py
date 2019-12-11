from django.shortcuts import render, get_object_or_404
from tweets.models import Tweet, Reply
from users.models import Follower, Profile
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count


# Create your views here.
# TODO: Turn all of these into Modals
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
