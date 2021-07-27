# Django
from django.conf import settings


tasks_default_settings = {
    "TODO_STAFF_ONLY": False,
}

def defaults(key: str):
    """Try to get a setting from project settings.
    If empty or doesn't exist, fall back to a value from defaults hash."""
    if hasattr(settings, key):
        return getattr(settings, key)
    return tasks_default_settings.get(key)

