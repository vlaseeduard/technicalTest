
# Internal
from .models import Task
from .defaults import defaults
from . import task_logger

def staff_check(user):
    """
    If TODO_STAFF_ONLY is set to True, limit view access to staff users only.
    """
    if defaults("TODO_STAFF_ONLY"):
        return user.is_staff
    # If unset or False, allow all logged in users
    return True


def user_can_read_task(task, user):
    return task.task_list.group in user.groups.all() or user.is_superuser


def toggle_task_completed(task_id: int) -> bool:
    """Toggle the `completed` bool on Task from True to False or vice versa."""
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return True
    except Task.DoesNotExist:
        task_logger.info(f"Task {task_id} not found.")
        return False

