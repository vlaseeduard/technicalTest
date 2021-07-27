# py
import datetime
# django
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
# Internal
from ..models import Task, TaskList
from ..utils import staff_check

@login_required
@user_passes_test(staff_check)
def list_lists(request) -> HttpResponse:
    """
        Homepage view - list of lists a user can view, and ability to add a list.
    """
    thedate = datetime.datetime.now()

    # Make sure user belongs to at least one group.
    if not request.user.groups.all().exists():
        messages.warning(
            request,
            "You do not yet belong to any groups. Ask your administrator to add you to one.",
        )

    # Superusers see all lists
    lists = TaskList.objects.all().order_by("group__name", "name")
    if not request.user.is_superuser:
        lists = lists.filter(group__in=request.user.groups.all())

    list_count = lists.count()

    # superusers see all lists, so count shouldn't filter by just lists the admin belongs to
    if request.user.is_superuser:
        task_count = Task.objects.filter(completed=0).count()
    else:
        task_count = (
            Task.objects.filter(completed=0)
            .filter(task_list__group__in=request.user.groups.all())
            .count()
        )

    return render(request, "module_task/list_lists.html", {
        "lists": lists,
        "thedate": thedate,
        "list_count": list_count,
        "task_count": task_count,
    })
