from django.contrib import admin

from users.models import Profile, Follower

admin.site.register(Profile)
admin.site.register(Follower)
