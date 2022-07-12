from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    caption    = models.TextField()
    image   = models.ImageField(upload_to = 'post/', default='./static/blank-profile-picture-973460_640.png')
    author  = models.ForeignKey( User, on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField(User, related_name="likes", blank=True, null=True)

    tags = TaggableManager()

    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.caption} by {self.author}"
    def get_absolute_url(self):
        return reverse("post:post_view", kwargs={
            "username": self.author.username,
            "post_id": self.id

            })


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"comment by {self.name} on {self.post}"

