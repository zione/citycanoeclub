from django.contrib import admin
from .models import RouteInfo
# Register your models here.


class RouteAdmin(admin.ModelAdmin):
    list_display = ['name','create_time','route_type','status']
    list_filter = ['create_time','route_type']


admin.site.register(RouteInfo, RouteAdmin)
