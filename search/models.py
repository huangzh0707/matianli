# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TopList(models.Model):
    top_project = models.CharField(max_length=200)

class SearchResults(models.Model):
    project_name = models.CharField(max_length=200)
    project_brief = models.CharField(max_length=500)

