from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    def __str__(self):
        return self.title
    def get_url(self):
        return "/question/{}/".format(self.id)
      
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
