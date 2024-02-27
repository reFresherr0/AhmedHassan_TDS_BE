from django.db import models

# Create your models here.
class Tags(models.Model):
    name=models.CharField(max_length=200)


class AttachedTags(models.Model):
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)

    # class Meta:
    #     unique_together=(('user_id','tag'),)