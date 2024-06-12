from django.db import models
from django.utils.text import slugify
from src.accounts.models import User
from django.conf import settings


class Conversation(models.Model):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="convo_starter",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="convo_participant",
    )
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="message_sender",
    )
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)


class Room(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.room.name + " - " + str(self.user.username) + " : " + str(self.message)
        )
