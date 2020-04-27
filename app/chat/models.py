from django.db import models
from django.contrib.auth import get_user_model

from core.models import TimeStampedModel as CoreModel
from post.models import Post

User = get_user_model()


class Room(CoreModel):
    name = models.CharField(max_length=30)
    id = models.TextField(primary_key=True, unique=True)
    members = models.ManyToManyField(User, related_name="room_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def messages(self):
        return self.room_messages


class Message(CoreModel):
    content = models.TextField()
    room = models.ForeignKey(Room, related_name="room_messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sender_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver_messages", on_delete=models.CASCADE)

