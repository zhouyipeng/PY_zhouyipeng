from django.db import models

# Create your models here.

class HeroInfo(models.Model):
    heroname = models.CharField(max_length=30)
    herolv = models.IntegerField(default=1)

    def __str__(self):
        return self.heroname


class SkillsInfo(models.Model):
    skill = models.CharField(max_length=30)
    atk = models.IntegerField(default=10)
    hero = models.ForeignKey(HeroInfo, on_delete=models.CASCADE)
