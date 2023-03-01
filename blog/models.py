from distutils import text_file
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return f"{self.title} by {self.author}"

class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.comment[0:5]}... by {self.user.username}"


    
