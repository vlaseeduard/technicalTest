"""module_user URL Configuration

The `urlpatterns` list routes URLs to views.

"""
# Django
from django.urls import path, include
# Internal
from . import views

app_name = "module_user"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.signup, name="signup")
]

