from django.contrib import admin

from models import Profile, Followers

# Register your models here.
admin.site.register(Profile, Followers)