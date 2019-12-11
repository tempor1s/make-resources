from django.contrib import admin

from models import Tweet, Reply

# Register your models here.
admin.site.register(Tweet, Reply)