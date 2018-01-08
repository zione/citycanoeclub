from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import RouteInfo
# Create your views here.


def routes_list(ListView):
    template_name = 'route/list.html'
    module = RouteInfo


def route_detail(DetailView):
    module = RouteInfo
    template_name = 'route/detail.html'