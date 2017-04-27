# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TopList(models.Model):
    company = models.CharField(max_length= 500)
    amount = models.PositiveIntegerField(default=0)
    rounds = models.CharField(max_length= 200)
    date = models.DateField('funding date')

class Profile(models.Model):
    toplist = models.ForeignKey(TopList, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
