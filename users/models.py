from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='pfp.jpg', upload_to='images/profile_pictures')

    def __str__(self):
        returns self.user.username

    @property
    def followers(self):
        # returns a count of the followers this profile has
        return Followers.objects.filter(following_user=self.user).count()
    
    @property
    def following(self):
        # returns the count of people this user is following
        return Followers.objects.filter(user=self.user).count()
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # TODO: Document
        super().save()

        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.weight > 300:
            # Save the image as 300px x 300px
            img.thumbnail((300, 300))
            img.save(self.image.path)


class Followers(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='following_user', on_delete=models.CASCADE)
    date_followed = models.DateTimeField(auto_now_add=True)