from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_profile

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_profile, name='register'),
    path('profile/', user_profile, name='profile'),
]