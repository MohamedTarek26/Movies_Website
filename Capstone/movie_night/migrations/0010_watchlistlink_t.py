# Generated by Django 3.1.2 on 2020-11-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_night', '0009_watchlistlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlistlink',
            name='t',
            field=models.TextField(null=True),
        ),
    ]
