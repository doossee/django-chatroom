from django.urls import path
from django.views.generic import TemplateView
from src.chat import views


urlpatterns = [
    path("start/", views.start_convo, name="start_convo"),
    path("<int:convo_id>/", views.get_conversation, name="get_conversation"),
    path("", views.conversations, name="conversations"),
]
