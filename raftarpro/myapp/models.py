from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class studentsdata(models.Model):
    roll_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=100)

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
