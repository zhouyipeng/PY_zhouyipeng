from django.db import models

# Create your models here.

class BookInfo(models.Model):
    titie = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now=True)

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    centent = models.CharField(max_length=30)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)



