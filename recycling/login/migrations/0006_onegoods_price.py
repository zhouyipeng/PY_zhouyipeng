# Generated by Django 2.2.3 on 2019-07-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_onegoods'),
    ]

    operations = [
        migrations.AddField(
            model_name='onegoods',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]