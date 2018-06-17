from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')                                                           
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(default="", max_length=225)
    text = models.TextField(default="")
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    objects = QuestionManager()
    def __unicode__(self):
          return self.title
    def get_url(self):
          return "/question/{}".format(self.id)
    
class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(null=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
