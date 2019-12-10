from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(max_length=280)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:10]
    
    @property
    def reply_count(self):
        return Reply.objects.filter(post_connected=self).count()

# TODO: Eventally just turn replies into individual tweets, but this will be easier for now
class Reply(models.Model):
    content = models.TextField(max_length=280)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Tweet, on_delete=models.CASCADE)