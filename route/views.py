from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import RouteInfo
# Create your views here.


class RouteList(ListView):
    template_name = 'route/list.html'
    model = RouteInfo
    paginate_by = 2

    def get_queryset(self):
        return RouteInfo.published.all()


class RouteDetail(DetailView):
    model = RouteInfo
    template_name = 'route/detail.html'

