from django.db import models

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=False,blank=False)
    allowed_users = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_over=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.id:
            if self.allowed_users < 5:
                self.name = "E-" + self.name
            elif 5<self.allowed_users <= 10:
                self.name = "N-" + self.name
            else:
                self.name = "P-" + self.name
        super().save(*args, **kwargs)

