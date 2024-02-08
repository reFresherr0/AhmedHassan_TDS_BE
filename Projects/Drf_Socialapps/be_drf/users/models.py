from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):

    def create_user(self, email, name, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, name, username, password=None):
        if password is None:
            raise TypeError('Password should not be None')
        user = self.create_user( email, name, username, password)
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES= (
        ('M','Male'),
        ('F','Female'),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=120)
    name= models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    mobile= PhoneNumberField()
    image = models.ImageField(blank=True,null=True)
    gender = models.CharField(max_length=1,null=True,blank=True,choices=GENDER_CHOICES)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    objects = UserManager()
