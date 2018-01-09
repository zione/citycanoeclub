from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class PublishedRouteManager(models.Manager):
    def get_queryset(self):
        return super(PublishedRouteManager,self)\
            .get_queryset().filter(status='published')


class RouteInfo(models.Model):
    ROUTE_TYPE = (
        ('field','Field'),
        ('city','City'),
    )

    STATUS_TYPE = (
        ('draft','Draft'),
        ('check','Check'),
        ('published','Published'),
        ('unshelve','Unshelve'),
    )

    name = models.CharField(max_length=64)
    desc = models.TextField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True, db_index=True)
    update_time = models.DateTimeField(auto_now=True)
    explorers = models.ManyToManyField(User, related_name='routes', blank=True)
    poster = models.ImageField(upload_to='poster/%Y/%m/%d',blank=True)
    users_like = models.ManyToManyField(User, related_name='routes_like', blank=True)
    route_type = models.CharField(max_length=20,choices=ROUTE_TYPE,default='city')
    status = models.CharField(max_length=30,choices=STATUS_TYPE,default='draft')

    objects = models.Manager()
    published = PublishedRouteManager()

    class Meta:
        ordering = ('-create_time',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('route:route_detail', args=[str(self.id)])
