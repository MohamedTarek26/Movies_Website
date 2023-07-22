from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import int_list_validator
# Create your models here.

class User(AbstractUser):
    pass

class watchListLink(models.Model):
    p=models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    m=models.IntegerField(null=True)
    t=models.TextField(blank=False,null=True)
class Review(models.Model):
    movieId=models.IntegerField(default=0)
    movieName=models.TextField(blank=False)
    publisher=models.ForeignKey('User',related_name="REVIEWS",on_delete=models.CASCADE,null=True)
    Post_text=models.TextField(max_length=1000,blank=False)
    movieType=models.TextField(blank=False,null=True)
