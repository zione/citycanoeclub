from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RouteInfo(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True,db_index=True)
    update_time = models.DateTimeField(auto_now=True)
    explorers = models.ManyToManyField(User,related_name='routes',blank=True)
    poster = models.ImageField(upload_to='poster/%Y/%m/%d',blank=True)
    users_like = models.ManyToManyField(User,related_name='routes_like',blank=True)
    route_type = models.PositiveIntegerField()