# Generated by Django 3.1.2 on 2020-11-19 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_night', '0006_auto_20201120_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='WatchList',
        ),
        migrations.AddField(
            model_name='integer',
            name='WatchListed_By',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MyWatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]