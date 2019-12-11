"""make_resources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # for the admin panel
from django.contrib.auth import views as auth_views # authentication views
from django.urls import path, include # for basic path stuff
from users import views as user_views # for profile and user based views
# static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Api
    path('api/', include('api.urls')),
    # Admin Site
    path('admin/', admin.site.urls),
    # Use Tweet Application for / route.
    path('', include('tweets.urls')),
    # User Auth Views
    path('', include('users.urls'))
]

# for static files in debug mode
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # for css, js, and other static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for profile pictures and other 'media'