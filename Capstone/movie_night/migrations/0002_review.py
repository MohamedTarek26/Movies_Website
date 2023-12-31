# Generated by Django 3.1.2 on 2020-11-16 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_night', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField(default=0)),
                ('movieName', models.TextField()),
                ('Post_text', models.TextField(max_length=1000)),
                ('likes', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='REVIEWS', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
