from django.db import models

# Create your models here.


class PollsInfo(models.Model):
    vote = models.CharField(max_length=100)
    votetime = models.DateField(auto_now=True)



class VoteInfo(models.Model):
    # 投票类别
    category = models.CharField(max_length=30)
    # 票数
    num = models.IntegerField(default=0)
    poll = models.ForeignKey(PollsInfo, on_delete=models.CASCADE)



