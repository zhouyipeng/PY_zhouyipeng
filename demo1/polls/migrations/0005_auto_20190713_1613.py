# Generated by Django 2.2.3 on 2019-07-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190713_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollsuser',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pollsuser',
            name='useractive',
            field=models.BooleanField(default=False),
        ),
    ]
