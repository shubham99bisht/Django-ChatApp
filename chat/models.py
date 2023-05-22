from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message