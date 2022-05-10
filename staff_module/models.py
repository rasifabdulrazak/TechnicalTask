from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=10, unique=True)
   
