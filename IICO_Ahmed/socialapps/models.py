from django.db import models
from users.models import User

# Create your models here.

class SocialApps(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=400)
    link= models.TextField()
    logo = models.ImageField(null=True,blank=True)
    sequence=models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)


class Clicks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    social_app= models.ForeignKey(SocialApps,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)