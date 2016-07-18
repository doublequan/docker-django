from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.TextField()
    link = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=200)
    source_link = models.TextField()
    description = models.TextField()
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.source + " : " + self.title + " TAG: " + self.tag


class Statistic(models.Model):
    total_post_num = models.IntegerField(default=0)
    fuck = models.CharField(max_length=100, default='fuck')


# class Source(models.Model):
#     source_name = models.CharField(max_length=200)
#     source_link = models.TextField()