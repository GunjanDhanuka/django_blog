from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # we don't use timezone.now() since we don't want to execute the function, only pass it as an argument to the DateTimeField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ##if user is deleted, delete the post.

    def __str__(self):
        return self.title
