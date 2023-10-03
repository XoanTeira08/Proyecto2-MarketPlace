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