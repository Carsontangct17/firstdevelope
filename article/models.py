from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class fz_classic(models.Model):
    name = models.CharField(max_length=56)
    articecount = models.IntegerField()
    def __unicode__(self):
        return self.name


class fz_Article(models.Model):
    title = models.CharField(max_length=56,verbose_name='title')
    content = models.TextField(verbose_name='contents')
    author = models.ForeignKey(User)
    tags = models.CharField(max_length=1023,verbose_name='label',blank=True)
    classic = models.ForeignKey(fz_classic)
    publish_date = models.DateTimeField()
    ispublished = models.BooleanField()
    commentcount = models.IntegerField(blank=True)
    readcount = models.IntegerField(blank=True)

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    ph = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    # return name



class fz_comment(models.Model):
    article = models.ForeignKey(fz_Article)
    comment_content = models.TextField()
    comment_date = models.DateField()
    email = models.EmailField()
    commentator = models.TextField()
# Create your models here.
