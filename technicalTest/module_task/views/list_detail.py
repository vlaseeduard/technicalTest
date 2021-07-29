# 3rd party
import bleach
# Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# internal
from ..forms import AddEditTaskForm
from ..models import Task, TaskList
from ..utils import staff_check
from ..service import CountriesWrapper

@login_required
@user_passes_test(staff_check)
def list_detail(request, list_id=None, list_slug=None, view_completed=False) -> HttpResponse:
    """
    Display and manage tasks in a todo list.
    """

    # Defaults
    task_list = None
    form = None

    # Which tasks to show on this list view?
    if list_slug == "mine":
        tasks = Task.objects.filter(assigned_to=request.user)

    else:
        # Show a specific list, ensuring permissions.
        task_list = get_object_or_404(TaskList, id=list_id)
        if task_list.group not in request.user.groups.all() and not request.user.is_superuser:
            raise PermissionDenied
        tasks = Task.objects.filter(task_list=task_list.id)

    # Additional filtering
    if view_completed:
        tasks = tasks.filter(completed=True)
    else:
        tasks = tasks.filter(completed=False)

    # ######################
    #  Add New Task Form
    # ######################

    if request.POST.getlist("add_edit_task"):
        form = AddEditTaskForm(
            request.user,
            request.POST,
            initial={"assigned_to": request.user.id, "priority": 999, "task_list": task_list},
        )

        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.created_by = request.user
            new_task.note = bleach.clean(form.cleaned_data["note"], strip=True)
            form.save()

            #todo Send email alert only if Notify checkbox is checked AND assignee is not same as the submitter

            messages.success(request, 'New task "{t}" has been added.'.format(t=new_task.title))
            return redirect(request.path)

    # Don't allow adding new tasks on some views
    if list_slug not in ["mine", "recent-add", "recent-complete"]:
        form = AddEditTaskForm(
            request.user,
            initial={"assigned_to": request.user.id, "priority": 999, "task_list": task_list},
        )

    return render(request, "module_task/list_detail.html", {
        "list_id": list_id,
        "list_slug": list_slug,
        "task_list": task_list,
        "form": form,
        "tasks": tasks,
        "view_completed": view_completed,
        "countries": CountriesWrapper().get_countries()
    })
