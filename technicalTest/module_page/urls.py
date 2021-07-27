"""module_user URL Configuration

The `urlpatterns` list routes URLs to views.

"""
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = "module_page"

urlpatterns = [

    path('', login_required(TemplateView.as_view(template_name="index.html")), name="index"),

]