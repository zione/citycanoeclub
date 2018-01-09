from django.urls import path
from . import views

app_name = 'route'

urlpatterns = [
    path('', views.RouteList.as_view(),name='route_list'),
    path('<int:pk>/', views.RouteDetail.as_view(), name='route_detail'),
]