# Generated by Django 2.2.3 on 2019-07-17 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_cartgoods'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartgoods',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.RecyclingUser'),
            preserve_default=False,
        ),
    ]
