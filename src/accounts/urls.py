from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path("", user_views.user_list, name="user_list"),
]
