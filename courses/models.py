from __future__ import unicode_literals

from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    count = models.IntegerField(default=0)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Course(models.Model):
    name = models.CharField(max_length=128)
    id = models.CharField(max_length=7, primary_key=True)
    # syllabus = models.CharField()
    # books = models.ListField()
    # prereq = models.ListField()
    # grades = models.models.ListField()
    # tags = models.ListField()
    # comments = models.ListField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


