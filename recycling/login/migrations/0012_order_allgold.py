# Generated by Django 2.2.3 on 2019-07-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_usermsg_usergold'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='allgold',
            field=models.IntegerField(default=0),
        ),
    ]