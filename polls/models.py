import datetime

from django.db import models

# Create your models here.
from django.utils import timezone

LEVEL_CHOICES=[
    ("easy", "easy"),
    ("normal", "normal"),
    ("hard", "hard")
]


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(verbose_name="publication date")
    is_active = models.BooleanField(default=True)
    level = models.CharField(max_length=200, choices=LEVEL_CHOICES, null=True, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="question/images/%Y/%m/%d")


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


