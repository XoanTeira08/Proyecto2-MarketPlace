from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name= 'User Profile'
    
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

class CustomerSupport(models.Model):
    class Meta:
        verbose_name_plural = 'Customer Support'
        verbose_name= 'Customer Support'

    name= models.CharField(max_length=50, blank=True, null=True)
    phone= models.CharField(max_length=10)
    email= models.EmailField(max_length=50)
    message= models.TextField(max_length=500)