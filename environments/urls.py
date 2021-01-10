"""Data_Solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

"""


from django.urls import path
from .views import UserEnvView, EnvDetailView, EnvCreateView, EnvUpdateView, EnvDeleteView, EnvListView
from . import views


urlpatterns = [
    path('', views.home, name='env-home'),
    path('user/<str:username>', UserEnvView.as_view(), name='user-env'),
    path('detail/<int:pk>/', EnvDetailView.as_view(), name='env-detail'),
    path('env_form/', EnvCreateView.as_view(), name='env-create'),
    path('env/<int:pk>/update/', EnvUpdateView.as_view(), name='env-update'),
    path('env/<int:pk>/delete/', EnvDeleteView.as_view(), name='env-delete'),
    path('about/', views.about, name='env-about'),
]