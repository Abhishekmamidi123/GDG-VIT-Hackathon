# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    year = models.IntegerField()
    rollno = models.IntegerField(unique=True)
    name = models.CharField(max_length=25)
    interns = models.IntegerField()
    workshops = models.IntegerField()
    clubs = models.IntegerField()
    score = models.FloatField()
    eventsorganized = models.IntegerField()
