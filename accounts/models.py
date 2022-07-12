from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    about = models.TextField()
    image = models.ImageField(upload_to = "profile/images/")
    def __str__(self):
        return f"{self.user.username}'s profile"


class UserRelation(models.Model):   
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User,on_delete=models.CASCADE, related_name="followers")

    def __str__(self):
        return f"{self.follower.username} is following {self.following.username}"