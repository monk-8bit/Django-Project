from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from blog.models import Post
# PW: Testpass88


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("Title: {} , Author: {}".format(self.title, self.author))
