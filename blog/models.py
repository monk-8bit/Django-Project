from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from blog.models import Post
# PW: Testpass88


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("Title: {} , Author: {}".format(self.title, self.author))

    # After Post is Created
    # Return the URL as a string, let the View do the Redirect
    def get_absolute_url(self):
        # return path to specific post
        return reverse('Post-Detail', kwargs={"pk": self.pk})
