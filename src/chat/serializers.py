from rest_framework import serializers
from src.accounts.serializers import UserSerializer
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ("conversation_id",)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ["initiator", "receiver", "last_message"]

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ["initiator", "receiver", "message_set"]
