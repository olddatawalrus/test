from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author_img_path = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    post_date = models.CharField(max_length=255)
    post_link = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    preview_img_path = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=255)
    
    
    def __unicode__(self):
       return ('post_preview', (),
            {
               'author_img_path': self.author_img_path,
               'author_name': self.author_name,
               'post_date': self.post_date,
               'post_link': self.post_link,
               'post_title': self.post_title,
               'preview_img_path': self.preview_img_path,
               'preview_text': self.preview_text,
            })
