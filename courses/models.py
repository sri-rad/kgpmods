from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=128)
    id = models.CharField(max_length=7, primary_key=True,unique=True)
    credits = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    grades = models.CharField(max_length=100)
    prereq = models.CharField(max_length=100)
    syllabus = models.TextField()

    def __unicode__(self):
        return self.id