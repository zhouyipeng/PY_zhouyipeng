from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PollsInfo(models.Model):
    vote = models.CharField(max_length=100)
    votetime = models.DateField(auto_now=True)

    def __str__(self):
        return self.vote


class VoteInfo(models.Model):
    # 投票类别
    category = models.CharField(max_length=30)
    # 票数
    num = models.IntegerField(default=0)
    poll = models.ForeignKey(PollsInfo, on_delete=models.CASCADE)

class PollsUser(User):
    telephone = models.CharField(max_length=11)










