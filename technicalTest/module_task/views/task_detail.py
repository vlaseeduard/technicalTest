#py
import datetime
import os
# 3rd party
import bleach
# django
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
# Internal
from ..defaults import defaults
from ..forms import AddEditTaskForm
from ..models import Task
from ..utils import (
    staff_check,
    toggle_task_completed,
    user_can_read_task,
)

@login_required
@user_passes_test(staff_check)
def task_detail(request, task_id: int) -> HttpResponse:
    """
        View task details. Allow task details to be edited.
    """
    task = get_object_or_404(Task, pk=task_id)

    # Ensure user has permission to view task. Superusers can view all tasks.
    # Get the group this task belongs to, and check whether current user is a member of that group.
    if not user_can_read_task(task, request.user):
        raise PermissionDenied

    # Save task edits
    if not request.POST.get("add_edit_task"):
        form = AddEditTaskForm(request.user, instance=task, initial={"task_list": task.task_list})
    else:
        form = AddEditTaskForm(
            request.user, request.POST, instance=task, initial={"task_list": task.task_list}
        )

        if form.is_valid():
            item = form.save(commit=False)
            item.note = bleach.clean(form.cleaned_data["note"], strip=True)
            item.title = bleach.clean(form.cleaned_data["title"], strip=True)
            item.save()
            messages.success(request, "The task has been edited.")
            return redirect(
                "todo:list_detail", list_id=task.task_list.id, list_slug=task.task_list.slug
            )

    # Mark complete
    if request.POST.get("toggle_done"):
        results_changed = toggle_task_completed(task.id)
        if results_changed:
            messages.success(request, f"Changed completion status for task {task.id}")
        return redirect("module_task:task_detail", task_id=task.id)


    return render(request, "module_task/task_detail.html", {
        "task": task,
        "form": form,
        "thedate": task.due_date if task.due_date else datetime.datetime.now(),
        "comment_classes": defaults("TODO_COMMENT_CLASSES"),
    })
