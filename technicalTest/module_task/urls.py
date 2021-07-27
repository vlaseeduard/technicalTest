"""module_task URL Configuration

The `urlpatterns` list routes URLs to views.

"""
# Django
from django.urls import path
# Internal
from . import views

app_name = "module_task"

urlpatterns = [
    path("", views.list_lists, name="lists"),
    path("add_list/", views.add_list, name="add_list"),
    path("<int:list_id>/<str:list_slug>/", views.list_detail, name="list_detail"),
    path("<int:list_id>/<str:list_slug>/completed/", views.list_detail, {"view_completed": True}, name="list_detail_completed",),
    path("<int:list_id>/<str:list_slug>/", views.list_detail, name="list_detail"),
    path("<int:list_id>/<str:list_slug>/delete/", views.del_list, name="del_list"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("toggle_done/<int:task_id>/", views.toggle_done, name="task_toggle_done"),
]

