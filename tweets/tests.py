from django.test import TestCase
from tweets.models import Tweet, Reply
from users.models import User

# Create your tests here.
class TweetTests(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_tweet_create(self):
        user = User.objects.create()
        tweet = Tweet.objects.create(content='this is tweet', author=user)

        tweet_from_db = Tweet.objects.all()[:1].get()

        # checks if the string representation of the tweet is accurate
        self.assertEqual('this is tw', str(tweet_from_db))

    def test_tweet_detail_page(self):
        user = User.objects.create()
        tweet = Tweet.objects.create(content='test tweet', author=user)

        tweet_page = self.client.get(f'/tweet/1/')

        self.assertEqual(tweet_page.status_code, 302)