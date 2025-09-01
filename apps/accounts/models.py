from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .manager import CustomUserManager
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser,PermissionsMixin):
  username=None
  id = models.AutoField(primary_key=True)
  email = models.EmailField( unique = True)
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  phone_no = models.CharField(max_length = 10,unique=True,null=False)
  ROLE_CHOICES = (
        ("admin", "Admin"),
        ("buyer", "Buyer"),
        ("supplier", "Supplier"),
    )
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="buyer")
  
  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['phone_no']


  
  def __str__(self):
      return "{}".format(self.email)



class BlacklistedToken(models.Model):
    token_string = models.CharField(max_length=30, unique=True)
    exp = models.IntegerField()


class ActiveToken(models.Model):
    token_string = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    exp = models.IntegerField()