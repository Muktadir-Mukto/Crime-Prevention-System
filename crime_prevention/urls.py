"""crime_prevention URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from crime_prevention import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home_menu.urls')),
    path('admin/', admin.site.urls),
    path('SIGNUP_LOGIN/', include('SIGNUP_LOGIN.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('department/', include('department.urls')),
    path('crime/', include('crime.urls')),
    path('criminal/', include('Criminal.urls')),
    path('post/', include('post.urls')),





]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


