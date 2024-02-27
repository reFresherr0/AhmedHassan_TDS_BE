from django.db import models

# Create your models here.

class SocialApps(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=400)
    link= models.TextField()
    logo = models.ImageField(null=True,blank=True)
    sequence=models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)


class Clicks(models.Model):
    # user_id = models.ForeignKey(User)
    social_app= models.ForeignKey(SocialApps,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)