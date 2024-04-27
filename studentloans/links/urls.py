from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
]