# Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.contrib.auth.models import Group
# Internal
from ..forms import AddTaskListForm
from ..utils import staff_check


@login_required
@user_passes_test(staff_check)
def add_list(request) -> HttpResponse:
    """
    Allow users to add a new
        #todo list to the group they're in.
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    if not request.user.is_staff:
        raise PermissionDenied

    if request.POST:
        form = AddTaskListForm(request.user, request.POST)
        if form.is_valid():
            try:
                newlist = form.save(commit=False)
                newlist.slug = slugify(newlist.name, allow_unicode=True)
                newlist.save()
                messages.success(request, "A new list has been added.")
                return redirect("module_task:lists")

            except IntegrityError:
                messages.warning(
                    request,
                    "There was a problem saving the new list. "
                    "Most likely a list with the same name in the same group already exists.",
                )



    return render(request, "module_task/add_list.html", {
        "form": AddTaskListForm(request.user, initial={"group": Group.objects.all()})
    })
