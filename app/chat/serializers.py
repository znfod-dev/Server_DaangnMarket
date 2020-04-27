from rest_framework import serializers

from chat.models import Room, Message
from post.serializers import PostSerializer


class RoomSerializer(serializers.ModelSerializer):

    post = PostSerializer(read_only=True)

    class Meta:
        model = Room
        fields = (
            'name', 'id', 'members', 'post'
        )


class RoomCreateSerializer(serializers.ModelSerializer):

    post = PostSerializer(read_only=True)

    class Meta:
        model = Room
        fields = (
            'name', 'id', 'post'
        )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('room', 'content', 'created', 'sender', 'receiver')


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'content',
        )
