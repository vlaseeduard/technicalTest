# django
from django.contrib import admin
# internal
from .models import Task, TaskList

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task_list", "completed", "priority", "due_date")
    list_filter = ("task_list",)
    ordering = ("priority",)
    search_fields = ("title",)


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList)


