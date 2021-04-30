from django.db import models

# Create your models here.
class Chat(models.Model):
  room_name = models.CharField(max_length=120)

  def __str__(self):
    return str(self.room_name)

  def get_messages(self):
    return self.messages.all()


class ChatMessage(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
  user = models.CharField(max_length=120)
  text = models.TextField()

  def __str__(self):
    return f"{self.chat.room_name}- {self.user}"
