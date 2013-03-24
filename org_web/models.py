from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Content(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    main_nav = models.BooleanField()
    url_key = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    """
    Symbolic links will actually link to a route and are simply for making navigation items for them dynamically
    """
    symbolic = models.TextField(default="no")

    def __str__(self):
        return self.title

class News(models.Model):
    posted = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=128)
    short = models.TextField()
    body = models.TextField()
    by = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Officer(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    picture = models.ImageField(upload_to=settings.OFFICER_IMG_PATH)
    postion = models.CharField(max_length=128)
    bio = models.TextField()

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)
