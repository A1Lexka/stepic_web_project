from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')                                                           
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    objects = QuestionManager()
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
