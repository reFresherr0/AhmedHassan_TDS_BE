from django.db import models
import uuid

# Create your models here.
class ActivationKeys(models.Model):
    KIND_CHOICES=(
        ('Bands','Bands'),
        ('Cards','Cards'),
        ('Keychains','Keychains'),
        ('IICO tags','IICO tags'),
    )
    kind =  models.CharField(max_length=50,choices=KIND_CHOICES)
    name = models.CharField(max_length=200,blank=True,null= True)
    activation_random_key= models.CharField(max_length=100,default=uuid.uuid4,editable=False,unique=True)
    active = models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)

class ActivationKeysAttached(models.Model):
    activation_id=models.OneToOneField(ActivationKeys,on_delete=models.RESTRICT)
    # user= models.ForeignKey(User)
    created_at=models.DateTimeField(auto_now_add=True)
