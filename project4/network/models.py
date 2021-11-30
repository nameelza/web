from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

def __str__(self):
    return self.username 


class Posts(models.Model):
    content = models.TextField()
    date =  models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likers = models.ManyToManyField(User, related_name='liked', blank=True)
    likesCount = models.IntegerField(default=0)

def __str__(self):
    return self.content

class User_Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.user.username + " follows " + self.follower.username



