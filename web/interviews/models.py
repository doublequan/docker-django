from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.TextField()
    link = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=200)
    desc = models.TextField()
    tag = models.CharField(max_length=200)


class Statistic(models.Model):
    total_post_num = models.IntegerField(default=0)
    fuck = models.CharField(max_length=100, default='fuck')
