from django.db import models
from rest_framework.authentication import get_user_model
# Create your models here.
class Notification(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)