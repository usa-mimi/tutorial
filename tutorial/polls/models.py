import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    class Meta:
        verbose_name = '質問'
        verbose_name_plural = '質問の複数形'
        ordering = ['-pub_date']

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
