from django.db import models
from users.models import User

# Create your models here.

class Notification(models.Model):
    user_to = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE, null=True, blank=True)
    user_from = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    is_connection_request = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    is_read = models.BooleanField(default=False)    
    
    def __str__(self):
        return str(self.user_to)+' You got a notification from '+ str(self.user_from)+ ' Message text: ' + str(self.message)
