"""technicalTest URL Configuration

The `urlpatterns` list routes URLs to views.

"""
# Django
from django.contrib import admin
from django.urls import path, include
# Internal
from .service import get_installed_modules_to_add_to_installed_apps

urlpatterns = [
    path('admin/', admin.site.urls),
]

for item in get_installed_modules_to_add_to_installed_apps():
    urlpatterns.append(path(f"{item.replace('module_', '')}/", include(f'{item}.urls')))
    print(f'Dynamically adding URL definitions for module: {item}')