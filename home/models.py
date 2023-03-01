from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Contactus(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.email}"

class profile(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50, blank=True)
    backup_email = models.CharField(max_length=150, blank=True)
    another_phone = models.CharField(blank=True, max_length=50)
    bio = models.CharField(blank=True, max_length=150)
    address = models.CharField(blank=True, max_length=150)
    pic = models.ImageField(blank=True,default='static/img/user.png')
    dob = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.nick_name}'s profile"