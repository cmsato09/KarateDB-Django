from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import logged_in_dashboard

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', logged_in_dashboard, name='dashboard'),
]
